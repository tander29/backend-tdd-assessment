import argparse
import sys


def help_this():
    print("help")


def lower_text(text):
    return text.lower()


def upper_text(text):
    return text.upper()


def title_text(text):
    return text.title()


def create_argparser():
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase',
        action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase',
        action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase',
        action='store_true')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main():
    parser = create_argparser()
    args = parser.parse_args()

    if not args:
        parser.print_help()
        sys.exit()

    text = args.text

    if args.upper:
        text = upper_text(args.text)

    if args.lower:
        text = lower_text(args.text)

    if args.title:
        text = title_text(args.text)

    return text


if __name__ == "__main__":
    print (main())
