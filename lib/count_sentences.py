import sys
import io
import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    
    def is_sentence(self):
        return self._value.endswith('.')

    
    def is_question(self):
        return self._value.endswith('?')

    
    def is_exclamation(self):
        return self._value.endswith('!')

   
    def count_sentences(self):
        sentences = re.split(r'[.!?]+', self._value)
        
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

        return len(sentences)