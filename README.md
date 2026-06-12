# **Simple Calculator**

A command-line calculator application written in Python that performs basic arithmetic operations using an Object-Oriented Programming structure.

---

## Features
- **Addition**: Add two numbers  
- **Subtraction**: Subtract two numbers  
- **Multiplication**: Multiply two numbers  
- **Division**: Divide two numbers with zero-division protection  
- **Chain Calculation**: Automatically reuse the previous result  
- **Decimal Support**: Supports floating-point values  
- **Interactive Menu**: Easy-to-use and clean command-line interface  
- **Memory Reset**: Clear the stored result anytime  

---

## Requirements
- Python 3.6 or higher  

---

## Installation
1. Clone or download the project
2. Navigate to the project directory:
   ```cd simple_calculator_python```

### Windows
```bash
python simple_calculator.py
```

### macOS / Linux
```bash
python3 simple_calculator.py
```
--- 

## How to Use

1. Select an operation from the menu:

    1, Addition  
    2. Subtraction  
    3. Multiplication  
    4. Division  
    5. Clear Memory  

2. Enter your choice  

3. Enter the required two numbers  

4. The result will be displayed  

5. Choose whether to proceed with another calculation (`y/n`)  

6. If you continue, the calculator automatically stores the previous result  

7. Select **Clear Memory** to reset the stored value  

8. Select `n` to exit the application

---

## Example

```text
╔══════════════════════════════╗
║         🧮 CALCULATOR        ║
╠══════════════════════════════╣
║  1. ➕ Addition              ║
║  2. ➖ Subtraction           ║
║  3. ✖️ Multiplication        ║
║  4. ➗ Division              ║
║  5. 🗑️ Clear Memory          ║
╠══════════════════════════════╣
║  Stored: None               ║
╚══════════════════════════════╝

Choose an operation (1-5): 1
Enter the first number: 2
Enter the second number: 3

Result: 5.0

Do you want to continue? (y/n): n

Thank you for using the calculator. Goodbye! xoxo
```
---

## Error Handling
The calculator prevents:
- Empty input  
- Invalid number input  
- Division by zero  
- Invalid menu selections  

---

## Project Structure

```text
simple_calculator_python/
│── math_operation/
│   ├── interface.py
│   ├── main.py
│   ├── math_operation.py
│   └── simple_calculator.py
└── README.md
```
