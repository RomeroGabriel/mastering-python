import re

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text: str):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for word in self.words:
            yield word

sentence = Sentence("Corinthians Lakers Liverpool")

for word in sentence:
    print(word)