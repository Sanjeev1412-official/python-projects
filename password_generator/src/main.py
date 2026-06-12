import sys
import generator

def get_boolean_choice(prompt: str) -> bool:
    """Prompts the user for a yes/no option and returns a boolean equivalent."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ('y', 'yes', ''):  # Pressing Enter defaults to Yes
            return True
        if choice in ('n', 'no'):
            return False
        print("Invalid choice! Please input 'y' for Yes or 'n' for No.")

def main() -> None:
    print("=== Cryptographically Secure Password Generator ===")
    
    try:
        # 1. Extract and validate requested length
        length_input = input("Enter desired password length (minimum 4, recommended 12+): ").strip()
        if not length_input.isdigit():
            print("Error: Length must be a positive whole number.", file=sys.stderr)
            sys.exit(1)
            
        pwd_length = int(length_input)

        # 2. Extract boolean options
        print("\n--- Configure Complexity Settings ---")
        use_upper = get_boolean_choice("Include Uppercase Characters? (Y/n): ")
        use_digits = get_boolean_choice("Include Numeric Digits? (Y/n): ")
        use_symbols = get_boolean_choice("Include Special Symbols/Punctuation? (Y/n): ")

        # 3. Execute generator call
        secure_password = generator.generate_secure_password(
            length=pwd_length,
            include_uppercase=use_upper,
            include_digits=use_digits,
            include_specialchar=use_symbols
        )

        # 4. Display result cleanly
        print("\n================ PASSWORD ================")
        print(f"Generated Password: {secure_password}")
        print("===============================================")
        
    except ValueError as config_err:
        print(f"\nConfiguration Error: {config_err}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nSession aborted by user. Exiting safely.")
        sys.exit(0)

if __name__ == "__main__":
    main()