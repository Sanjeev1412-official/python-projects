import sys
from typing import List
from model import Questions
from engine import QuizEngine

def load_sample_dataset() -> List[Questions]:
    
    return [
        Questions(
            text="Which keyword is used to define a function in Python?",
            choises=["func", "define", "def", "function"],
            answer=2
        ),
        Questions(
            text="What is the correct file extension for standard Python files?",
            choises=[".pt", ".py", ".pyt", ".pyc"],
            answer=1
        ),
        Questions(
            text="Which Python data structure is unordered, mutable, and unique?",
            choises=["List", "Tuple", "Dictionary", "Set"],
            answer=3
        )
    ]

def get_validated_choice(prompt: str, choice_limit: int) -> int:

    while True:
        try:
            val = int(input(prompt).strip())
            if 1 <= val <= choice_limit:
                return val - 1  
            print(f"Out of bounds! Please enter an integer between 1 and {choice_limit}.")
        except ValueError:
            print("Invalid Input! Please enter a valid number.", file=sys.stderr)

def main() -> None:
    print("=== Production-Ready Python Quiz App ===")
    
    
    questions = load_sample_dataset()
    quiz = QuizEngine(questions)
    
    try:
        
        while not quiz.is_completed():
            question = quiz.get_current_question()
            
            print(f"\nQuestion: {question.text}")
            for idx, choice in enumerate(question.choises, start=1):
                print(f"  {idx}. {choice}")
                
            
            user_selection = get_validated_choice("\nSelect your option (number): ", len(question.choises))
            
            
            correct = quiz.submit_answer(user_selection)
            
            if correct:
                print("✨ Correct!")
            else:
                correct_answer_str = question.choises[question.answer]
                print(f"❌ Incorrect. The right answer was: {correct_answer_str}")
                
    
        print("\n================ SESSION COMPLETE ================")
        print(f"Final Score: {quiz.score} / {quiz.total_questions}")
        percentage = (quiz.score / quiz.total_questions) * 100
        print(f"Success Rating: {percentage:.1f}%")
        print("==================================================")
        
    except KeyboardInterrupt:
        print("\nSession terminated abruptly. Exiting safely.")
        sys.exit(0)

if __name__ == "__main__":
    main()