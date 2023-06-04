from secrets import choice
from math import ceil
import string

alphabet = list(string.ascii_lowercase)

class Cipher:
    def __init__(self, key=None):
        self.key = ''
        if key is None:
            for i in range(100):
                self.key += choice(alphabet)
        else:
            self.key = key

    def encode(self, text):

        if len(self.key) < len(text):
            adjusted_key = self.key * ceil(len(text)/len(self.key))
        else:
            adjusted_key = self.key

        res = ''
        for index, letter in enumerate(text):

            new_index = alphabet.index(letter) + alphabet.index(adjusted_key[index])
            
            while (new_index > 25):
                new_index -= 26

            res += alphabet[new_index]

        return res


    def decode(self, text):

        if len(self.key) < len(text):
            adjusted_key = self.key * ceil(len(text)/len(self.key))
        else:
            adjusted_key = self.key

        res = ''
        for index, letter in enumerate(text):
            new_index = alphabet.index(letter) - alphabet.index(adjusted_key[index]) 

            while (new_index < 0):
                new_index += 26

            res += alphabet[new_index]

        return res
