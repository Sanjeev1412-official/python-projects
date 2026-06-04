import sys
import checker as checker


def main(prompt: str) -> int:

    # if prompt is not a number, print an error message and exit
    if prompt == "" or not prompt.isdigit():
        print("Input must be an integer.")
        sys.exit(1)
    even = checker.is_even_odd(prompt)

    return "EVEN" if even else "ODD"


if __name__ == "__main__":
    prompt = input("Enter a number: ").strip()
    result = main(prompt)
    print(result)
