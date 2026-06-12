from typing import List
from model import Questions

class QuizEngine:
    def __init__(self, questions: List[Questions]) -> None:
        if not questions:
            raise ValueError("The quiz must contain at least one question.")
            
        self._questions = questions
        self._current_index = 0
        self._score = 0

    @property
    def score(self) -> int:
        return self._score

    @property
    def total_questions(self) -> int:
        return len(self._questions)

    def is_completed(self) -> bool:
        return self._current_index >= len(self._questions)

    def get_current_question(self) -> Questions:
        if self.is_completed():
            raise IndexError("No more questions remaining in this session.")
        return self._questions[self._current_index]

    def submit_answer(self, user_choice_idx: int) -> bool:
        current_q = self.get_current_question()
        is_correct = user_choice_idx == current_q.answer
        
        if is_correct:
            self._score += 1
            
        self._current_index += 1
        return is_correct