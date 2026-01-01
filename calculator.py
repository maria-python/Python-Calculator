import sys  # import system-specific parameters and functions
from PyQt5.QtWidgets import (  # import PyQt5 GUI components
   QApplication, QMainWindow, QWidget,
   QVBoxLayout, QGridLayout, QPushButton, QLabel
)
from PyQt5.QtCore import Qt  # import Qt constants for alignment and orientation




class Calculator(QMainWindow):  # create main window class inheriting from QMainWindow
   def __init__(self):  # constructor for the calculator
       super().__init__()  # initialize parent class QMainWindow


       self.setWindowTitle("Calculator")  # set the window title
       self._central = QWidget(self)  # create a central widget
       self.setCentralWidget(self._central)  # set central widget for main window


       # ===== Core Variables =====
       self.current = ""  # current input number
       self.operator = None  # current operator (+, -, ×, ÷)
       self.A = None  # first operand for calculations


       # ===== Display =====
       self.display_label = QLabel("0", self)  # create a display label initialized with 0
       self.display_label.setAlignment(Qt.AlignRight)  # align text to the right
       self.display_label.setStyleSheet("font-size: 40px; padding: 10px;")  # style the display


       # ===== Layouts =====
       main_layout = QVBoxLayout()  # vertical layout for main window
       main_layout.addWidget(self.display_label)  # add display label to main layout


       button_layout = QGridLayout()  # grid layout for buttons


       # List of button labels for calculator
       buttons = [
           ["AC", "+/-", "%", "÷"],  # top row special buttons
           ["7", "8", "9", "×"],     # numbers row
           ["4", "5", "6", "-"],     # numbers row
           ["1", "2", "3", "+"],     # numbers row
           ["0", ".", "√", "="],     # bottom row numbers and functions
       ]


       # Create buttons and add them to the grid
       for row_idx, row in enumerate(buttons):  # iterate over rows
           for col_idx, label in enumerate(row):  # iterate over columns
               btn = QPushButton(label, self)  # create button with label
               btn.setFixedSize(80, 60)  # set fixed size for button


               # ===== Style buttons =====
               if label in ["AC", "+/-", "%"]:  # light gray for special buttons
                   btn.setStyleSheet("background-color: #D4D4D2; color: black; font-size: 20px;")
               elif label in ["÷", "×", "-", "+", "="]:  # orange for operators
                   btn.setStyleSheet("background-color: #FF9500; color: white; font-size: 20px;")
               else:  # dark gray for number buttons
                   btn.setStyleSheet("background-color: #505050; color: white; font-size: 20px;")


               # Connect button click to handler
               btn.clicked.connect(lambda _, v=label: self.on_button_click(v))  # pass label to handler
               button_layout.addWidget(btn, row_idx, col_idx)  # add button to grid at position


       main_layout.addLayout(button_layout)  # add button grid to main layout
       self._central.setLayout(main_layout)  # set layout for central widget
       self.setFixedSize(self.sizeHint())  # fix window size to prevent resizing


   def on_button_click(self, value):  # handle button clicks
       if value in "0123456789":  # number buttons
           if self.current == "0":  # if current is 0, replace it
               self.current = value
           else:  # otherwise append the number
               self.current += value
           self.display_label.setText(self.current)  # update display


       elif value == ".":  # decimal point
           if "." not in self.current:  # add decimal if not present
               self.current += "."
               self.display_label.setText(self.current)  # update display


       elif value in ["+", "-", "×", "÷"]:  # operator buttons
           try:
               self.A = float(self.current)  # store first operand
           except ValueError:
               self.A = 0  # default to 0 if conversion fails
           self.operator = value  # store operator
           self.current = ""  # reset current input
           self.display_label.setText("0")  # reset display


       elif value == "=":  # equals button
           if self.A is not None and self.current != "":  # ensure operands exist
               B = float(self.current)  # second operand
               result = 0  # initialize result
               if self.operator == "+":  # addition
                   result = self.A + B
               elif self.operator == "-":  # subtraction
                   result = self.A - B
               elif self.operator == "×":  # multiplication
                   result = self.A * B
               elif self.operator == "÷":  # division
                   if B != 0:  # avoid division by zero
                       result = self.A / B
                   else:
                       result = "Error"
               self.display_label.setText(str(result))  # show result
               self.current = str(result)  # store result as current
               self.operator = None  # reset operator
               self.A = None  # reset first operand


       elif value == "AC":  # clear button
           self.current = ""  # reset current
           self.operator = None  # reset operator
           self.A = None  # reset first operand
           self.display_label.setText("0")  # reset display


       elif value == "+/-":  # change sign
           if self.current.startswith("-"):  # remove negative if present
               self.current = self.current[1:]
           else:  # add negative if not zero
               if self.current != "0":
                   self.current = "-" + self.current
           self.display_label.setText(self.current)  # update display


       elif value == "%":  # percentage
           try:
               val = float(self.current)  # convert to float
               val /= 100  # divide by 100
               self.current = str(val)  # store as string
               self.display_label.setText(self.current)  # update display
           except:
               pass  # ignore errors


       elif value == "√":  # square root
           try:
               val = float(self.current)  # convert to float
               val = val ** 0.5  # calculate square root
               self.current = str(val)  # store as string
               self.display_label.setText(self.current)  # update display
           except:
               pass  # ignore errors




if __name__ == "__main__":  # main entry point
   app = QApplication(sys.argv)  # create Qt application
   calc = Calculator()  # create calculator instance
   calc.show()  # show the calculator window
   sys.exit(app.exec_())  # start the event loop