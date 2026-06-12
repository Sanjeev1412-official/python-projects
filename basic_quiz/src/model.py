from typing import List
class Questions:
    def __init__(self, text : str , choises: List[str], answer: int):

        if not text.strip():
            raise ValueError("Question cannot be empty")
        if len(choises) < 2:
            raise ValueError("choices must be at least 2")
        if not( 0 <= answer < len(choises)):
            raise ValueError("Question cannot be empty")

        self.text = text
        self.choises = choises
        self.answer = answer