import argparse


def init_parser():
    parser = argparse.ArgumentParser(
        'Returns intent behind the phrase (Supported lang: polish).\nExample: "jeszcze jak" -> "tak"\nUse -h for help.')

    parser.add_argument('-s', type=str, help='Sentence to get intent from(str).')
    parser.add_argument('-i', type=str, help='Path to .txt file containing sentence to get intent from.')
    parser.add_argument('', type=str, help='Path to .txt file containing sentence to get intent from.')

    return parser


def parse_input(argv):
    h_parser = init_parser()
    parsed = h_parser.parse_args(argv)
    return parsed.i
