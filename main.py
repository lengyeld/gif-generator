import pathlib
import time

import click
from generator import generate_gif


@click.command()
@click.argument("video_path", type=click.Path(exists=True, path_type=pathlib.Path))
@click.option(
    "--frame_number",
    "-f",
    type=click.INT,
    default=50,
    help="The number of frames that will be used for the GIF",
)
def main(video_path, frame_number):
    print("Starting...")
    start_time = time.time()
    generate_gif(video_path, frame_number)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
