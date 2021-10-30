import imageio


def main():
    print("Starting...")
    reader = imageio.get_reader("sample.mp4")

    with imageio.get_writer("sample.gif", mode="I") as writer:
        for (i, img) in enumerate(reader):
            print(f"Frame #{i}")
            writer.append_data(img)


if __name__ == "__main__":
    main()
