from setuptools import setup

setup(
    name="image-qa-checker",
    version="0.1.0",
    py_modules=["image_qa"],
    install_requires=["Pillow"],
    entry_points={
        "console_scripts": [
            "image-qa=image_qa:main",
        ]
    },
)
