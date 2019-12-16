from html_generator import build_html_generator


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    # parser.add_argument("--mode", type=str, choices=['single', 'multiple'], help='To display a single image folder or Compare multiple image folders.')
    parser.add_argument("--dirs", type=str, nargs='+', help="Input can be a image folder or a flist text file.")
    parser.add_argument("--keyword", type=str, nargs='+', default='', help="Keyword of image name")
    parser.add_argument("--ext", type=tuple, nargs='+', default=('.png', '.jpg'), help="Extension of image name")
    parser.add_argument("--width", type=int, default=256, help="Display width on html page")
    parser.add_argument("--output", type=str, help="Output html file")
    args = parser.parse_args()
    return args


def img2html():
    args = parse_args()
    html_generator = build_html_generator(args)
    html_generator.generate()


if __name__ == "__main__":
    img2html()
