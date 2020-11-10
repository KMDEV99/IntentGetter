#! /usr/bin/python3

import click
from classification_dict import classification_dict
from intent_getter import create_regex, get_intent


@click.command()
@click.option('--sentence', '-s', help='Sentence to get intent from(str).', default="")
@click.option('--path', '-p', help='Path to .txt file containing sentence to get intent from(str).', default="")
def main(sentence, path):
    classification_regex = create_regex(classification_dict.keys())
    print(get_intent(sentence, classification_regex))


if __name__ == "__main__":
    main()
