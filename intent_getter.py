from re import match, compile
from classification_dict import classification_dict


def create_regex(word_list):
    sentence_regex = "|".join([r"\b" + key + r"\b" for key in word_list])
    return compile(sentence_regex)


def get_intent(text, compiled_sentence_regex):
    intent = "brak"
    matched = match(pattern=compiled_sentence_regex, string=text)
    if matched:
        found_sentence = matched[0]
        intent = classification_dict[found_sentence]
    return intent
