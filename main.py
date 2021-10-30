import imageio


GIF_FIXED_FRAMES = 50


def main():
    print("Starting...")
    reader = imageio.get_reader("sample.mp4")

    total_frames = get_total_frames(reader)
    step = round(total_frames / GIF_FIXED_FRAMES)
    count = 0

    with imageio.get_writer("sample.gif", mode="I") as writer:
        for (i, img) in enumerate(reader):
            if i % step == 0:
                count += 1
                print(f"Frame #{i}")
                writer.append_data(img)

    print(f"count: {count}")


def get_total_frames(reader):
    """
    Won't always return with the exact number!
    If it can not get the total frames from reader.get_length() then
    it will try to guess it based on FPS and video duration.
    """

    total_frames = reader.get_length()
    if total_frames != float("inf"):
        return total_frames

    meta = reader.get_meta_data()
    fps = meta.get("fps")
    duration = meta.get("duration")

    return round(fps * duration)


if __name__ == "__main__":
    main()
