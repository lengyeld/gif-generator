import pathlib
import threading
from multiprocessing import Queue
from typing import List

import imageio
import imutils
from imutils.video.count_frames import count_frames


def generate_gif(video: pathlib.Path, frame_number: int):
    reader = imageio.get_reader(video)

    total_frames = count_frames(str(video))
    step = round(total_frames / frame_number)

    processed_frames = Queue(maxsize=frame_number)

    indexes = [i for i in range(0, total_frames, step)]
    threading.Thread(
        target=_read_frames,
        args=(reader, processed_frames, indexes),
        daemon=True,
    ).start()

    file_name = video.with_suffix(".gif")
    with imageio.get_writer(file_name, mode="I") as writer:
        for _ in indexes:
            frame = processed_frames.get(block=True)
            writer.append_data(frame)


def generate_thumbnail(video: pathlib.Path):
    reader = imageio.get_reader(video)

    frame = reader.get_data(0)
    frame = imutils.resize(frame, width=600)

    file_name = video.with_suffix(".jpg")
    imageio.imwrite(file_name, frame)


def _read_frames(reader, processed_frames: Queue, indexes: List[int]):
    for index in indexes:
        frame = reader.get_data(index)
        frame = imutils.resize(frame, width=600)
        processed_frames.put(frame)
