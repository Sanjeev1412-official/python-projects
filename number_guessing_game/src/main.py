import sys
from number_guessing_game import GuessingGameEngine

def get_valid_guess(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val <= value <= max_val:
                return value
            print(f"Out of bounds! Please enter a whole number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a valid whole integer.", file=sys.stderr)

def main() -> None:
    low, high = 1, 100
    print(f"I am thinking of a number between {low} and {high}. Can you find it?")
    
    game = GuessingGameEngine(lower_bound=low, upper_bound=high)
    
    try:
        while True:
            user_guess = get_valid_guess(f"Enter your guess ({low}-{high}): ", low, high)
            
            result = game.check_guess(user_guess)

            if result == "TOO_LOW":
                print("Too low! Try a higher number.\n")
            elif result == "TOO_HIGH":
                print("Too high! Try a lower number.\n")
            elif result == "CORRECT":
                print(f"\n🎉 Congratulations! You guessed it in {game.attempts} attempts.")
                break
                
    except KeyboardInterrupt:
        print("\nGame terminated by user. Thanks for playing!")
        sys.exit(0)

if __name__ == "__main__":
    main()