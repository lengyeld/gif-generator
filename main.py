import threading
import time
from queue import Queue
from typing import List

import imageio
import imutils
from imutils.video.count_frames import count_frames


GIF_FIXED_FRAMES = 50


def main():
    print("Starting...")
    reader = imageio.get_reader("sample.mp4")

    total_frames = count_frames("sample.mp4")
    step = round(total_frames / GIF_FIXED_FRAMES)

    processed_frames = Queue(maxsize=GIF_FIXED_FRAMES)

    indexes = [i for i in range(0, total_frames, step)]
    threading.Thread(
        target=read_frames,
        args=(reader, processed_frames, indexes),
    ).start()

    with imageio.get_writer("sample.gif", mode="I") as writer:
        for i in indexes:
            frame = processed_frames.get(block=True)
            print(f"Writing frame #{i}")
            writer.append_data(frame)


def read_frames(reader, processed_frames: Queue, indexes: List[int]):
    for index in indexes:
        frame = reader.get_data(index)
        frame = imutils.resize(frame, width=600)
        processed_frames.put(frame)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
