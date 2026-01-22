#!/usr/bin/env python
import os
import argparse
from PIL import Image

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg"}

def check_image(path, aspect_ratio, min_width):
    issues = []

    name, ext = os.path.splitext(os.path.basename(path))
    if ext.lower() not in ALLOWED_EXTENSIONS:
        issues.append("unsupported file type")

    if not name.replace("_", "").isalnum():
        issues.append("bad filename format")

    try:
        with Image.open(path) as img:
            width, height = img.size

            if width < min_width:
                issues.append(f"width < {min_width}px")

            expected_w, expected_h = aspect_ratio
            if round(width / height, 2) != round(expected_w / expected_h, 2):
                issues.append("wrong aspect ratio")
    except Exception:
        issues.append("cannot read image")

    return issues


def run(folder, aspect_ratio, min_width):
    if not os.path.isdir(folder):
        print(f"Folder not found: {folder}")
        return

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)
        if not os.path.isfile(full_path):
            continue

        issues = check_image(full_path, aspect_ratio, min_width)
        if issues:
            print(f"❌ {file} → {', '.join(issues)}")
        else:
            print(f"✅ {file} → OK")


def main():
    parser = argparse.ArgumentParser(description="AI image output QA checker")
    parser.add_argument("folder", help="Folder containing images")
    parser.add_argument("--aspect", default="1:1", help="Aspect ratio (e.g. 1:1, 4:5)")
    parser.add_argument("--min-width", type=int, default=1024)

    args = parser.parse_args()
    w, h = map(int, args.aspect.split(":"))
    run(args.folder, (w, h), args.min_width)


if __name__ == "__main__":
    main()
