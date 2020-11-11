from re import findall, compile
from classification_dict import classification_dict
from unidecode import unidecode


class IntentGetter:
    def __init__(self):
        self.compiled_sentence_regex = compile("|".join([r"\b" + key + r"\b" for key in classification_dict.keys()]))

    def get_intent(self, text):
        intent = "brak"
        text = unidecode(text.replace(",", "").replace(".", "").lower())
        matched = findall(pattern=self.compiled_sentence_regex, string=text)
        if matched:
            found_sentence = matched[-1]
            intent = classification_dict[found_sentence]
        return intent
