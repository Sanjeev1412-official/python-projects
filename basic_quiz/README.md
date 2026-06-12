# Basic Python Quiz Application

A production-ready command-line Python Quiz Application. This demonstrate Object-Oriented Programming (OOP) concepts, input validation, and clean code architecture in Python.

## 🚀 Features

- **Interactive CLI**: Simple and intuitive command-line interface.
- **Robust Input Validation**: Safely handles invalid user inputs (e.g., non-integers, out-of-bounds choices) gracefully.
- **Clean Architecture**: Effectively separates concerns using individual modules for the data model (`model.py`), logic engine (`engine.py`), and presentation layer (`main.py`).
- **Score Tracking**: Calculates and displays the final score and success percentage at the end of the session.
- **Extensible**: Designed to make it easy to load external datasets or add new questions.

## 📁 Project Structure

```text
basic_quiz/
├── src/
│   ├── main.py       # Application entry point and CLI UI logic
│   ├── engine.py     # Core quiz engine and state management
│   └── model.py      # Data models and attribute validation
```

## 🛠️ Technologies Used

- **Language**: Python 3.12+

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have Python 3.12 or higher installed on your system.

### Steps to Run

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd basic_quiz
   ```

2. **Run the Application**:
   You can run the application directly using Python from the project root directory:
   ```bash
   python src/main.py
   ```

## 🎮 Usage Example

```text
=== Production-Ready Python Quiz App ===

Question: Which keyword is used to define a function in Python?
  1. func
  2. define
  3. def
  4. function

Select your option (number): 3
✨ Correct!

...

================ SESSION COMPLETE ================
Final Score: 3 / 3
Success Rating: 100.0%
==================================================
```

## 👨‍💻 Author

**Sanjeev1412-official**
- Email: sanjeevsnair1412official@gmail.com
- GitHub: [Sanjeev1412-official](https://github.com/Sanjeev1412-official)

---
*This project was created for educational purposes.*
