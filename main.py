#! /usr/bin/python3

import click
from intent_getter import IntentGetter


@click.command()
@click.option('--sentence', '-s', help='Sentence to get intent from(str).', default="")
@click.option('--path', '-p', help='Path to .txt file containing sentence to get intent from(str).', default="")
def main(sentence, path):
    ig = IntentGetter()

    if path:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    print("%s: %s" % (ig.get_intent(text=line), line))
        except FileNotFoundError:
            print("File: %s does not exists. Please enter proper path." % path)
    else:
        if not sentence:
            sentence = input("Enter sentence: ")
        print(ig.get_intent(text=sentence))


if __name__ == "__main__":
    main()
