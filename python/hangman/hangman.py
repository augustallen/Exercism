# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = [char for char in word]
        self.masked_word = "_"*len(word)

    def guess(self, char):
        if self.status == STATUS_WIN:
            raise ValueError("You have won.")
        if self.status == STATUS_LOSE:
            raise ValueError("You have lost.")
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
        if char not in self.word or char in self.masked_word:
            self.remaining_guesses -= 1
        for n, i in enumerate(self.word):
            if char == i:
                self.masked_word = self.masked_word[:n] + char + self.masked_word[n+1:]
        if "_" not in self.masked_word:
            self.status = STATUS_WIN
        return self.masked_word

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status