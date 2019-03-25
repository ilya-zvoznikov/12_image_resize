import argparse
from PIL import Image
import os
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description='Do not use --width/--height and --scale simultaneously')

    parser.add_argument(
        'input', help='path to original image')
    parser.add_argument(
        '--output', help='path to result image')
    parser.add_argument(
        '--width', type=int, help='result image width')
    parser.add_argument(
        '--height', type=int, help='result image height')
    parser.add_argument(
        '--scale', type=float, help='result and original image ratio')

    args = parser.parse_args()

    if all([args.scale, any([args.height, args.width])]):
        raise argparse.ArgumentParser.error(
            parser,
            message='Do not use width/height and scale simultaneously'
        )

    args_dict = {'height': args.height,
                 'width': args.width,
                 'scale': args.scale,
                 'output': args.output,
                 'input': args.input,
                 }

    return args_dict


def resize_image(original_image, height, width, scale):
    original_image_ratio = original_image.height / original_image.width

    if scale:
        result_height = int(original_image.height * scale)
        result_width = int(original_image.width * scale)
    elif width and height:
        result_width = width
        result_height = height
    elif width:
        result_width = width
        result_height = int(width * original_image_ratio)
    elif height:
        result_height = height
        result_width = int(height / original_image_ratio)
    else:
        result_width = original_image.width
        result_height = original_image.height

    result_image = original_image.resize((result_width, result_height))
    return result_image


def get_path_to_result(original_image, result_image):
    original_image_basename, original_image_ext = os.path.splitext(
        original_image.filename
    )
    result_image_basename = original_image_basename + '_{}x{}'.format(
        result_image.width, result_image.height
    )
    return result_image_basename + original_image_ext


if __name__ == '__main__':
    args = get_args()
    try:
        original_image = Image.open(args['input'])
    except IOError:
        sys.exit('Incorrect image file')

    result_image = resize_image(
        original_image=original_image,
        height=args['height'],
        width=args['width'],
        scale=args['scale'],
    )
    path_to_result = args['output']

    if not path_to_result:
        path_to_result = get_path_to_result(original_image, result_image)

    original_ratio = round(original_image.width / original_image.height, 2)
    result_ratio = round(result_image.width / result_image.height, 2)

    if original_ratio != result_ratio:
        print("width and height ratio has changed")

    try:
        result_image.save(path_to_result)
    except ValueError:
        sys.exit('Incorrect path to save')
