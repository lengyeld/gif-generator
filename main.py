import pathlib
import time

import click
from generator import generate_gif


@click.command()
@click.argument("video_path", type=click.Path(exists=True, path_type=pathlib.Path))
def main(video_path):
    print("Starting...")
    start_time = time.time()
    generate_gif(video_path)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
