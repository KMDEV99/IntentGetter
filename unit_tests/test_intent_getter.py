from unittest import TestCase
from intent_getter import *
from classification_dict import classification_dict


class Test(TestCase):
    def setUp(self):
        self.iG = intentGetter()

    def test_get_intent_one_word_tak(self):
        output = self.iG.get_intent("tak")
        self.assertEqual("tak", output)

    def test_get_intent_one_word_nie(self):
        output = self.iG.get_intent("nie")
        self.assertEqual("nie", output)

    def test_get_intent_one_word_niewiem(self):
        output = self.iG.get_intent("nie wiem")
        self.assertEqual("nie wiem", output)

    def test_get_intent_one_word_brak(self):
        output = self.iG.get_intent("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lor")
        self.assertEqual("brak", output)

    def test_get_intent_two_words_tak(self):
        output = self.iG.get_intent("mi tak")
        self.assertEqual("tak", output)

    def test_get_intent_uppercase(self):
        output = self.iG.get_intent("Od dzisiaj AbsoluTnie lubię poniedziałek")
        self.assertEqual("tak", output)

    def test_get_intent_special_characters(self):
        output = self.iG.get_intent("Lubię jeść marmoladę łyżką oraz oczywiście też źle")
        self.assertEqual("tak", output)

    def test_get_intent_all(self):
        for key, value in classification_dict.items():
            output = self.iG.get_intent(key)
            self.assertEqual(value, output, msg="%s: %s" % (key, output))

    def test_get_intent_ignore_special_characters(self):
        output = self.iG.get_intent("#@!tak#@!")
        self.assertEqual("tak", output)

    def test_get_intent_basic_sentences(self):
        example_dict = {
            "tak": "tak",
            "raczej nie": "nie",
            "nie wiem": "nie wiem",
            "oczywiście": "tak",
            "jak najbardziej": "tak",
            "w żadnym wypadku": "nie",
            "skąd mam wiedzieć": "nie wiem",
            "no trudno powiedzieć ale myślę, że w zasadzie to tak": "tak",
            "no trudno powiedzieć ale myślę, że w zasadzie to nie": "nie",
            "no trudno powiedzieć": "nie wiem",
            "no": "tak",
            "no nie wiem": "nie wiem",
            "cokolwiek innego": "brak",
            "czemu nie": "tak",
            "oczywiście, że nie": "nie",
            "nie widzę przeszkód": "tak",
        }
        for key, value in example_dict.items():
            output = self.iG.get_intent(key)
            self.assertEqual(value, output, msg="%s: %s" % (key, output))
