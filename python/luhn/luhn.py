class Luhn:
    def __init__(self, card_num):
        self.number = card_num.replace(' ', '')

    def double_it(self, number):
        return ((int(number) * 2) if (int(number) * 2 < 10) else ((int(number) * 2) - 9))

    def valid(self):

        # not valid if has only one digit or if chars are not numbers
        if len(self.number) == 1 or not self.number.isdigit(): 
            return False

        doubled = ''

        if len(self.number) % 2 == 0:
            parity = True
        else:
            parity = False

        for i in range(0, len(self.number), 1):
            if (parity and i % 2 == 0) or (not parity and i % 2 != 0):
                doubled += str(self.double_it(self.number[i]))
            else:
                doubled += self.number[i]

        return sum(map(lambda x: int(x), doubled)) % 10 == 0
