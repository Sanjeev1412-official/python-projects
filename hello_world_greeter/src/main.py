import sys
from greeter import greeter

def main() -> None:
    print("Hello, World!")
    try:
        name = input("Enter Your Name: ")
        greeter_msg = greeter(name)
        print(greeter_msg)
    except ValueError as error:
        print(f"Application error {error}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Application interrupted by user")
        sys.exit(0)

if __name__ == "__main__":
    main()