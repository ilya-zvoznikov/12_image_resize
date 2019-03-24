import argparse
from PIL import Image
import os


def get_args():
    parser = argparse.ArgumentParser(
        description='Do not use --width/--height and --scale simultaneously')

    parser.add_argument(
        '--input', required=True, help='path to original image')
    parser.add_argument(
        '--output', help='path to result image')
    parser.add_argument(
        '--height', type=int, help='result image height')
    parser.add_argument(
        '--width', type=int, help='result image width')
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
                 'output_path': args.output,
                 'input_path': args.input,
                 }

    return args_dict


def resize_image(path_to_original, path_to_result):
    pass


if __name__ == '__main__':
    args = get_args()
    print(args)