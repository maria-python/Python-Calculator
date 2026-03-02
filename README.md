# Desktop Calculator

Desktop GUI calculator application built with PyQt5 that performs basic arithmetic and utility operations through an intuitive graphical interface.

Designed to demonstrate practical experience in Python GUI development, event-driven programming, and application logic structuring.


## Business Problem

Many beginner-level applications focus only on backend logic, without demonstrating user interface implementation.

However, in real development environments:

- Tools often require user-friendly interfaces  
- Applications must respond to user interactions dynamically  
- Clear separation between UI and logic is important  
- State management is required for consistent behavior  

Understanding GUI architecture and event-driven programming is essential for building user-facing desktop tools.


## Solution

The Desktop Calculator is a fully functional GUI application developed using PyQt5.

The system:

- Provides a structured graphical layout using QVBoxLayout and QGridLayout  
- Handles button click events dynamically  
- Maintains internal state for operands and operators  
- Performs arithmetic operations in real time  
- Updates the display reactively based on user interaction  
- Manages error cases such as division by zero  

This project demonstrates practical implementation of desktop application development using Python.


## Key Features

- Graphical User Interface built with PyQt5  
- Event-driven button handling  
- Basic arithmetic operations (+, −, ×, ÷)  
- Square root calculation  
- Percentage calculation  
- Positive / negative toggle (+/-)  
- Clear (AC) functionality  
- Division-by-zero protection  
- Styled interface with custom button colors  
- Fixed window layout with responsive display  


## Tech Architecture

The project follows an object-oriented design:

- `Calculator` class inherits from `QMainWindow`  
- Layout management using `QVBoxLayout` and `QGridLayout`  
- Centralized event handling via `on_button_click()`  
- Internal state tracking:
  - Current input
  - Selected operator
  - Stored operand  

The architecture reflects structured GUI development principles and state-based logic handling.


## Tech Stack

- Python 3.9.6  
- PyQt5  
- Qt Framework  


## Project Structure

```
desktop_calculator/
│
├── main.py              # Application entry point
├── requirements.txt
└── README.md
```


## Installation

1. Clone the repository:

```
git clone https://github.com/maria-python/desktop_calculator.git
cd desktop_calculator
```

2. Install dependencies:

```
pip install PyQt5
```


## Usage

Run the application:

```
python main.py
```

The calculator window will open with a fully interactive interface.


## Workflow

1. Launch the application  
2. Enter numbers using the GUI buttons  
3. Select an operator  
4. Enter the second number  
5. Press "=" to calculate the result  
6. Use additional functions such as:
   - AC (clear)
   - +/- (toggle sign)
   - % (percentage)
   - √ (square root)

The display updates dynamically based on user interaction.


## Results

- Demonstrates GUI development skills using PyQt5  
- Shows understanding of event-driven programming  
- Implements structured state management  
- Simulates development of a small desktop utility  
- Strengthens frontend + backend logic integration in Python  


## Future Improvements

- Keyboard input support  
- Memory functions (M+, M-, MR)  
- Improved error messaging  
- Scientific calculator mode  
- Unit testing for calculation logic  
- Packaging as standalone executable (PyInstaller)  


## Author

Mariia Ilnitska  

Junior Python Automation / Tech Assistant  


## Contacts

Gmail: maria.ilnitska11@gmail.com  

LinkedIn: www.linkedin.com/in/maria-ilnitska  

Telegram: @mariailnitska
