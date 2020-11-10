from re import findall, compile
from classification_dict import classification_dict
from unidecode import unidecode

class intentGetter():
    def __init__(self):
        self.compiled_sentence_regex = compile("|".join([r"\b" + key + r"\b" for key in classification_dict.keys()]))

    def get_intent(self, text):
        intent = "brak"
        matched = findall(pattern=self.compiled_sentence_regex, string=unidecode(text.lower()))
        if matched:
            found_sentence = matched[-1]
            intent = classification_dict[found_sentence]
        return intent