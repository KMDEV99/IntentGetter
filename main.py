#! /usr/bin/python3

from sys import argv
import click
from classification_dict import classification_dict
from intent_getter import create_regex, get_intent

@click.command()
@click.option('--sentence', help='Sentence to get intent from(str).')
#@click.option('--path', help='Path to .txt file containing sentence to get intent from(str).')
def main(sentence):
    classification_regex = create_regex(classification_dict.keys())
    print(get_intent(sentence, classification_regex))


if __name__ == "__main__":
    main()
