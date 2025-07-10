# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = ''.join('_' for _ in self.word)

    def guess(self, char):
        
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        
        if char not in self.word or char in self.masked_word:
            self.remaining_guesses -= 1

        else:
            self._update_masked_word(char)

        self._update_game_status()

    def _update_masked_word(self, char):

        masked_word_list = list(self.masked_word)

        for i, word_char in enumerate(self.word):
            if word_char == char:
                masked_word_list[i] = char

        self.masked_word = ''.join(masked_word_list)

    def _update_game_status(self):

        if self.masked_word == self.word:
            self.status = STATUS_WIN

        if self.remaining_guesses == -1:
            self.status = STATUS_LOSE
        

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
