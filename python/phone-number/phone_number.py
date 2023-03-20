import re
from string import punctuation
class PhoneNumber:
    def __init__(self, number):

        # get numbers and area codes
        self.number = ''.join(filter(lambda x: x.isdigit(), number))
        self.area_code = self.number[:3]

        # check if there's a country code
        if len(self.number) == 11 and self.number[0] == '1':
            self.number = self.number[1:]
            self.area_code = self.number[1:4]
        elif len(self.number) == 11 and self.number[0] != '1':
            raise ValueError("11 digits must start with 1")
        
        # check for erros
        if re.search('[a-zA-Z]', number):
            raise ValueError("letters not permitted")
        elif any(char in punctuation.replace('-', '').replace('(','').replace(')', '').replace('.','').replace('+', '') for char in number):
            raise ValueError("punctuations not permitted")
        elif len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif self.number[0] == '0':
            raise ValueError("area code cannot start with zero")
        elif self.number[0] == '1':
            raise ValueError("area code cannot start with one")
        elif self.number[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        elif self.number[3] == '1':
            raise ValueError("exchange code cannot start with one")
        
    def pretty(self):
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'