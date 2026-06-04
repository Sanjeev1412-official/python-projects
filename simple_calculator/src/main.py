import contextlib
from ntpath import join
from calculator import add,sub,mul,div
import sys

def main() -> None:
    
    operations = {
        "+" : add,
        "-" : sub,
        "*" : mul,
        "/" : div
    }

    num1 = float(input("Enter the first number: "))

    print("\nAvailable Operations:\n")
    for key, value in operations.items():
        print(f"{key} : {value.__name__}")
    
    print("\n")

    choice = input("Enter your choice eg(add): ")

    choice_names = [op.__name__ for op in operations.values()]

    if choice not in choice_names:
        print("Error: Unsupported operation selected.", file=sys.stderr)
        sys.exit(1)

    
    if choice == "add":
        operation = "+"
    elif choice == "sub":
        operation = "-"
    elif choice == "mul":
        operation = "*"
    elif choice == "div":
        operation = "/"
    

        
    num2 = float(input("Enter the second number: "))

    try:
        calculation_func = operations[operation]
        result = calculation_func(num1, num2)
        if result == int(result):
            result = int(result)
        if num1 == int(num1):
            num1 = int(num1)
        if num2 == int(num2):
            num2 = int(num2)
        print(f"\nResult: {num1} {operation} {num2} = {result}")
        
    except ZeroDivisionError as err:
        print(f"\nExecution Failed: {err}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nSession aborted by user. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()