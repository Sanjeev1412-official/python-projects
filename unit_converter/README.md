# Production-Grade Unit Converter

A robust, command-line Python application designed to precisely convert scalar values between various physical units. This project showcases structured engineering, clean separation of concerns, and rigorous data validation.

## 🚀 Features

- **Multi-Category Support**: Seamlessly switch between converting lengths, weights, and temperatures.
- **Supported Units**:
  - **Length**: `meters`, `kilometers`, `miles`, `feet`, `inches`
  - **Weight**: `kilograms`, `grams`, `pounds`, `ounces`
  - **Temperature**: `celsius`, `fahrenheit`, `kelvin`
- **Extensible Architecture**: Utilizes a centralized registry mapping system. Adding new units requires zero logic changes for linear conversions.
- **Robust Input Validation**: Safely handles invalid inputs, prevents negative scales where inappropriate, and allows negative values for temperatures.
- **Clean Separation of Concerns**: Isolates the mathematical conversion logic (`engine.py`) from the user interface and input gathering (`main.py`).

## 📁 Project Structure

```text
unit_converter/
├── src/
│   ├── main.py       # Application entry point, UI, and input validation
│   └── engine.py     # Core mathematical conversions and registry
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
   cd unit_converter
   ```

2. **Run the Application**:
   Execute the tool directly via Python from the project root directory:
   ```bash
   python src/main.py
   ```

## 🎮 Usage Example

```text
=== Production-Grade Unit Converter ===

Categories:
1. Length
2. Weight
3. Temperature
Select category (1-3): 3

--- Temperature Conversion ---
Available Units: celsius, fahrenheit, kelvin

Enter source unit (Convert FROM): celsius
Enter target unit (Convert TO): fahrenheit
Enter the scalar value to convert: -10

================ CONVERSION OUTPUT ================
Result: -10.0 celsius = 14.0000 fahrenheit
===================================================
```

## 👨‍💻 Author

**Sanjeev1412-official**
- Email: [EMAIL_ADDRESS](sanjeevsnair1412official@gmail.com)
- GitHub: [Sanjeev1412-official](https://github.com/Sanjeev1412-official)

---
