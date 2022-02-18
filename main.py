import argparse
from echo1_image_slicer.echo1_image_slicer import slice_image


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Slices an image into smaller images.")
    parser.add_argument(
        "-f",
        "--file_name",
        help="The file name to slice.",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-sp",
        "--save_to_file_prefix",
        help="The prefix for saved slice file names.",
        required=False,
        type=str,
    )
    parser.add_argument(
        "-s",
        "--save_to_dir",
        help="The directory to save the slices to.",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-sw",
        "--slice_width",
        help="The width of each slice.",
        required=True,
        type=int,
    )
    parser.add_argument(
        "-sh",
        "--slice_height",
        help="The height of each slice.",
        required=True,
        type=int,
    )
    parser.add_argument(
        "-ow",
        "--overlap_width_ratio",
        help="The overlap width ratio.",
        default=0.2,
        type=float,
    )
    parser.add_argument(
        "-oh",
        "--overlap_height_ratio",
        help="The overlap height ratio.",
        default=0.2,
        type=float,
    )

    # python main.py -f ./tests/test.jpg -s ./output -sw 500 -sh 500
    args = vars(parser.parse_args())

    slice_image(
        file_name=args["file_name"],
        save_to_file_prefix=args["save_to_file_prefix"],
        save_to_dir=args["save_to_dir"],
        slice_width=args["slice_width"],
        slice_height=args["slice_height"],
        overlap_width_ratio=args["overlap_width_ratio"],
        overlap_height_ratio=args["overlap_height_ratio"],
    )
