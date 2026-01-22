# Image Output QA Checker

A small CLI tool to validate AI-generated image outputs before client delivery.

This tool is designed for workflows where images are generated in bulk and must meet strict delivery specifications such as aspect ratio, resolution, and filename consistency. It acts as a simple quality gate before uploading or sharing files.

---

## What it does

- Validates image aspect ratio (e.g. `1:1`, `4:5`)
- Checks minimum image width
- Ensures supported image formats (`.png`, `.jpg`, `.jpeg`)
- Flags invalid or inconsistent filenames
- Produces a clear pass/fail report for each file

This tool checks **deterministic properties only**. It does not evaluate visual quality.

---

## Why this exists

In AI image production workflows, a single incorrectly formatted image can lead to client rejection or costly rework.

This script is meant to catch those issues early, before delivery.

---

## Installation

Clone the repository and install locally:

```bash
pip install -e .
```
This installs the tool as a CLI command.

## Usage
```
image-qa <folder> --aspect <ratio> --min-width <pixels>
```

## Example
```
image-qa outputs --aspect 1:1 --min-width 1024
```


## Example Output
```
❌ wallpap_x4.png → wrong aspect ratio
❌ bed-final.jpg → bad filename format
✅ chair_002.png → OK
```

## Expected Folder Structure

The tool expects a folder containing generated image files:

```
outputs/
├── image_001.png
├── image_002.jpg
└── image_003.png
```

## Tradeoff

This tool validates only metadata and structure (dimensions, aspect ratio, filenames), not subjective visual quality.

This decision keeps the tool fast, deterministic, and easy to automate in production pipelines.

## Use Cases

AI-generated lifestyle images for e-commerce

Batch image generation pipelines

Pre-delivery QA checks

Internal tooling for image operators

## License
```
MIT License
```