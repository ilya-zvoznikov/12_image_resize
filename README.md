# Image Resizer

The app "Image Resizer" is intended to change height and width of your image.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt # alternatively try pip3
```

#Quickstart

The path to the original image file is specified when running after the script name.
Also you may specify height and (or) width of result image or scale.
Do not use scale and height (width) simultaneously.
If path to the result image is not specified the result image will be saved to the same path.

```bash
$ python image_resize.py google-logo.png --scale=2
# result - google-logo_1280x688.png in the same path
```

To see help use option '--help' or '-h'.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
