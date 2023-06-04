class Allergies:

    all = ['eggs',
            'peanuts',
            'shellfish',
            'strawberries',
            'tomatoes',
            'chocolate',
            'pollen',
            'cats']

    def __init__(self, score):
        while score > 256:
            score -= 256
        self.score = bin(score)[2:]

    def allergic_to(self, item):
        index = len(self.score) - 1

        for digit in self.score:

            if (digit == '1' and Allergies.all[index] == item):
                return True
            
            index -= 1
        
        return False

    @property
    def lst(self):
        res = []
        index = len(self.score) - 1

        for digit in self.score:

            if (digit == '1'):
                res += [Allergies.all[index]]
            
            index -= 1
        
        return res
 