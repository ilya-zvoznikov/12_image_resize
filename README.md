# Image Resizer

The app "Image Resizer" is intended to change height and width of your image.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt # alternatively try pip3
```

# Quickstart

The path to the original image file is specified when running after the script name.
Also you may specify _height_ and (or) _width_ of result image or _scale_.
Do not use _scale_ and _height_ (_width_) simultaneously.
If path to the result image is not specified the result image will be saved to the same path. 
If only _output_ is specified the result image will be equal original one.

```bash
$ python image_resize.py google-logo.png --scale=2
# result - google-logo_1280x688.png in the same path
```

To see help use option _--help_ or _-h_.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
