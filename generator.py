import pathlib
import threading
from queue import Queue
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
        target=read_frames,
        args=(reader, processed_frames, indexes),
    ).start()

    file_name = video.with_suffix(".gif")
    with imageio.get_writer(file_name, mode="I") as writer:
        for i in indexes:
            frame = processed_frames.get(block=True)
            print(f"Writing frame #{i}")
            writer.append_data(frame)


def read_frames(reader, processed_frames: Queue, indexes: List[int]):
    for index in indexes:
        frame = reader.get_data(index)
        frame = imutils.resize(frame, width=600)
        processed_frames.put(frame)
