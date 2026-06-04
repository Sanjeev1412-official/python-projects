import sys
from mul_gen import generate_multiplication

def display_formatted_table(size: int, matrix: list) -> None:

    max_value = size * size
    cell_width = len(str(max_value)) + 2  

    header_line = " " * cell_width + "".join(f"{i:>{cell_width}}" for i in range(1, size + 1))
    print(header_line)
    print(" " * cell_width + "-" * (size * cell_width))

    for idx, row in enumerate(matrix, start=1):
        row_str = f"{idx:<{cell_width}}|" + "".join(f"{val:>{cell_width}}" for val in row)
        print(row_str)

def main() -> None:
    try:
        size_input = input("Enter table grid size (e.g., 10 for a 10x10 grid): ").strip()
        if not size_input.isdigit():
            print("Error: Input must be a valid positive whole number.", file=sys.stderr)
            sys.exit(1)
            
        grid_size = int(size_input)
        matrix = generate_multiplication(grid_size)
        
        print("\nGenerated Matrix Layout:")
        display_formatted_table(grid_size, matrix)
        
    except ValueError as err:
        print(f"Configuration Error: {err}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nSession aborted. Exiting safely.")
        sys.exit(0)

if __name__ == "__main__":
    main()