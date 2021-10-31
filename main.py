import pathlib

import click
from yaspin import yaspin

from generator import generate_gif, generate_thumbnail


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
    with yaspin(text="Generating GIF...") as spinner:
        generate_gif(video_path, frame_number)
        spinner.write("✅ GIF generated")

        generate_thumbnail(video_path)
        spinner.write("✅ Thumbnail generated")

        spinner.text = ""


if __name__ == "__main__":
    main()
