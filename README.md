# Image Output QA Checker

A small utility to validate AI-generated image outputs before delivery.

## What it does
- Checks filename format
- Verifies resolution and aspect ratio
- Validates image file types
- Produces a clear pass/fail report

## Usage
```bash
pip install -r requirements.txt
python image_qa.py ./outputs --aspect 1:1 --min-width 1024
```

