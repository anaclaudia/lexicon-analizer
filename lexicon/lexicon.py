from nose.tools import *

verbs = [ 'go','drink','open','eat','dance','run','walk' ]
nouns = [ 'door', 'chair', 'table', 'book', 'botle', 'fork', 'knive', 'spoon']
directions = [ 'north', 'south', 'west', 'east' ]
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

class Lexicon(object):
    def convert_number(self, sentence):
        try:
            return int(sentence)
        except ValueError:
            return None

    def split(self, sentence):
      return sentence.split(" ")

    def scan(self, sentence):
        sentence_words = self.split(sentence)
        labeled_word = []
        for word in sentence_words:
            if self.convert_number(word):
                labeled_word.append(('number', word))
            elif word in verbs:
                labeled_word.append(('verb', word))
            elif word in nouns:
                labeled_word.append(('noun', word))
            elif word in directions:
                labeled_word.append(('direction', word))
            else:
                labeled_word = (('error', word))
        return labeled_word

lexicon = Lexicon()
result = lexicon.scan("1 go door south")
print result
