# Cryptographically Secure Password Generator

A robust command-line Python application designed to generate highly secure, random passwords. This project leverages Python's built-in `secrets` module to ensure cryptographically strong randomness, making the generated passwords suitable for managing sensitive data and accounts.

## 🚀 Features

- **Cryptographically Secure**: Uses `secrets.SystemRandom()` rather than the standard pseudo-random `random` module to ensure unpredictable password generation.
- **Customizable Length**: Allows users to specify the exact length of the password (minimum of 4 characters).
- **Complexity Settings**: Users can toggle the inclusion of:
  - Uppercase Characters (A-Z)
  - Numeric Digits (0-9)
  - Special Symbols & Punctuation (!@#$...)
- **Interactive CLI**: Provides a clean, step-by-step interactive prompt for easy configuration.
- **Graceful Error Handling**: Safely handles invalid inputs and allows the user to exit cleanly at any time.

## 📁 Project Structure

```text
password_generator/
├── src/
│   ├── main.py           # Application entry point and interactive CLI UI
│   └── generator.py      # Core password generation logic using the `secrets` module
```

## 🛠️ Technologies Used

- **Language**: Python 3.12+
- **Standard Libraries**: `secrets`, `string`, `sys`

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have Python 3.12 or higher installed on your system. No external packages are required as it relies purely on standard Python libraries.

### Steps to Run

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd password_generator
   ```

2. **Run the Application**:
   Execute the tool directly via Python from the project root directory:
   ```bash
   python src/main.py
   ```

## 🎮 Usage Example

```text
=== Cryptographically Secure Password Generator ===
Enter desired password length (minimum 4, recommended 12+): 16

--- Configure Complexity Settings ---
Include Uppercase Characters? (Y/n): y
Include Numeric Digits? (Y/n): y
Include Special Symbols/Punctuation? (Y/n): y

================ PASSWORD ================
Generated Password: K)9jL3j,%hU6aX@q
===============================================
```

## 👨‍💻 Author

**Sanjeev1412-official**
- Email: [EMAIL_ADDRESS](sanjeevsnair1412official@gmail.com)
- GitHub: [Sanjeev1412-official](https://github.com/Sanjeev1412-official)

---

