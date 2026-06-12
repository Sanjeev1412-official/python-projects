import sys
import engine

def get_float(prompt: str, allow_negative: bool = False) -> float:
    while True:
        try:
            val = float(input(prompt).strip())
            if not allow_negative and val < 0:
                print("Input Error: Value must be a positive number.")
                continue
            return val
        except ValueError:
            print("Invalid Input! Please enter a valid decimal or integer.", file=sys.stderr)

def get_menu_choice() -> int:
    while True:
        print("\nCategories:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        try:
            choice = int(input("Select category (1-3): ").strip())
            if 1 <= choice <= 3:
                return choice
            print("Invalid Input! Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid Input! Please enter a number.", file=sys.stderr)

def main() -> None:
    print("=== Production-Grade Unit Converter ===")
    
    try:
        choice = get_menu_choice()
        
        if choice == 1:
            category = "Length"
            units = list(engine.LENGTH_REGISTRY.keys())
            func = engine.convert_length
            allow_negative = False
        elif choice == 2:
            category = "Weight"
            units = list(engine.WEIGHT_REGISTRY.keys())
            func = engine.convert_weight
            allow_negative = False
        else:
            category = "Temperature"
            units = list(engine.TEMPERATURE_UNITS)
            func = engine.convert_temperature
            allow_negative = True

        print(f"\n--- {category} Conversion ---")
        print(f"Available Units: {', '.join(units)}\n")

        from_unit = input("Enter source unit (Convert FROM): ").strip()
        to_unit = input("Enter target unit (Convert TO): ").strip()
        
        input_value = get_float("Enter the scalar value to convert: ", allow_negative=allow_negative)
        
        result = func(input_value, from_unit, to_unit)

        print("\n================ CONVERSION OUTPUT ================")
        print(f"Result: {input_value} {from_unit} = {result:.4f} {to_unit}")
        print("===================================================")

    except ValueError as business_err:
        print(f"\nOperational Error: {business_err}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nSession aborted by user. Exiting safely.")
        sys.exit(0)

if __name__ == "__main__":
    main()