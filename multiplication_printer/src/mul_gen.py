from typing import List

def generate_multiplication(size : int) -> List[List[int]]:

    if size < 1:
        raise ValueError("SIZE MUST BE 1 OR MORE")
    elif size > 30:
        raise ValueError("SIZE MUST BE 30 OR LESS")
      
    return [[row * col for col in range(1, size + 1)] for row in range(1, size + 1)]
    