import argparse
from pathlib import Path

import cv2
import numpy as np


IMAGE_DIR = Path(__file__).resolve().parent / "images"


def images_are_equal(image1_path: Path, image2_path: Path) -> bool:
    image1 = cv2.imread(str(image1_path), cv2.IMREAD_UNCHANGED)
    image2 = cv2.imread(str(image2_path), cv2.IMREAD_UNCHANGED)
    if image1 is None:
        raise ValueError(f"Could not read image: {image1_path}")
    if image2 is None:
        raise ValueError(f"Could not read image: {image2_path}")
    if image1.shape != image2.shape:
        return False
    return bool(np.array_equal(image1, image2))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check whether two images have identical pixel content."
    )
    parser.add_argument(
        "image1",
        nargs="?",
        type=Path,
        default=IMAGE_DIR / "image-1.jpg",
        help="first image (default: images/image-1.jpg)",
    )
    parser.add_argument(
        "image2",
        nargs="?",
        type=Path,
        default=IMAGE_DIR / "image-3.jpg",
        help="second image (default: images/image-3.jpg)",
    )
    args = parser.parse_args()

    try:
        equal = images_are_equal(args.image1, args.image2)
    except (OSError, ValueError) as error:
        parser.exit(2, f"Could not compare images: {error}\n")

    if equal:
        print(f"SAME: {args.image1} and {args.image2} have identical pixels.")
        return 0

    print(f"DIFFERENT: {args.image1} and {args.image2} do not have identical pixels.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
