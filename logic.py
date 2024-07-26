import random

class GuessTheNumberGame:
    def __init__(self, range_start, range_end, attempts, initial_capital):
        self.range_start = range_start
        self.range_end = range_end
        self.attempts = attempts
        self.initial_capital = initial_capital
        self.secret_number = random.randint(self.range_start, self.range_end)
        self.capital = initial_capital

    def make_guess(self, guess, bet):
        if guess == self.secret_number:
            self.capital += bet
            return True, self.capital
        else:
            self.capital -= bet
            return False, self.capital

    def is_game_over(self):
        return self.attempts <= 0 or self.capital <= 0
