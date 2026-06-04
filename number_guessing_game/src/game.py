import random

class GuessingGameEngine:
    def __init__(self, lower_bound: int = 1, upper_bound: int = 100) -> None:

        if lower_bound >= upper_bound:
            raise ValueError("Lower bound must be strictly less than the upper bound.")
            
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self._target_number = random.randint(lower_bound, upper_bound)
        self.attempts = 0

    def check_guess(self, guess: int) -> str:
        self.attempts += 1
        
        if guess < self._target_number:
            return "TOO_LOW"
        elif guess > self._target_number:
            return "TOO_HIGH"
        else:
            return "CORRECT"

    def reset_game(self) -> None:
        self._target_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0