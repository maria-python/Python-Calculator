import sys  
from PyQt5.QtWidgets import (  
   QApplication, QMainWindow, QWidget,
   QVBoxLayout, QGridLayout, QPushButton, QLabel
)

from PyQt5.QtCore import Qt  

class Calculator(QMainWindow):  
   def __init__(self): 
       super().__init__()  

       self.setWindowTitle("Calculator")  
       self._central = QWidget(self)  
       self.setCentralWidget(self._central) 

       self.current = ""  
       self.operator = None  
       self.A = None  

       self.display_label = QLabel("0", self)  
       self.display_label.setAlignment(Qt.AlignRight)  
       self.display_label.setStyleSheet("font-size: 40px; padding: 10px;")  

       main_layout = QVBoxLayout()  
       main_layout.addWidget(self.display_label)  

       button_layout = QGridLayout()  

       buttons = [
           ["AC", "+/-", "%", "÷"],  
           ["7", "8", "9", "×"],   
           ["4", "5", "6", "-"],     
           ["1", "2", "3", "+"],   
           ["0", ".", "√", "="],     
       ]

       for row_idx, row in enumerate(buttons): 
           for col_idx, label in enumerate(row):  
               btn = QPushButton(label, self) 
               btn.setFixedSize(80, 60)  
              
               if label in ["AC", "+/-", "%"]:  
                   btn.setStyleSheet("background-color: #D4D4D2; color: black; font-size: 20px;")
               elif label in ["÷", "×", "-", "+", "="]: 
                   btn.setStyleSheet("background-color: #FF9500; color: white; font-size: 20px;")
               else:  
                   btn.setStyleSheet("background-color: #505050; color: white; font-size: 20px;")
               
               btn.clicked.connect(lambda _, v=label: self.on_button_click(v))  
               button_layout.addWidget(btn, row_idx, col_idx)  

       main_layout.addLayout(button_layout)
       self._central.setLayout(main_layout)  
       self.setFixedSize(self.sizeHint()) 

   def on_button_click(self, value):  
       if value in "0123456789":  
           if self.current == "0":  
               self.current = value
           else: 
               self.current += value
           self.display_label.setText(self.current)  

       elif value == ".":  
           if "." not in self.current:  
               self.current += "."
               self.display_label.setText(self.current) 

       elif value in ["+", "-", "×", "÷"]: 
           try:
               self.A = float(self.current)  
           except ValueError:
               self.A = 0 
           self.operator = value  
           self.current = ""  
           self.display_label.setText("0")  

       elif value == "=":  
           if self.A is not None and self.current != "": 
               B = float(self.current)  
               result = 0  
               if self.operator == "+":  
                   result = self.A + B
               elif self.operator == "-": 
                   result = self.A - B
               elif self.operator == "×":  
                   result = self.A * B
               elif self.operator == "÷": 
                   if B != 0: 
                       result = self.A / B
                   else:
                       result = "Error"
               self.display_label.setText(str(result))  
               self.current = str(result)  
               self.operator = None  
               self.A = None  

       elif value == "AC":  
           self.current = "" 
           self.operator = None  
           self.A = None  
           self.display_label.setText("0")  

       elif value == "+/-":  
           if self.current.startswith("-"):  
               self.current = self.current[1:]
           else: 
               if self.current != "0":
                   self.current = "-" + self.current
           self.display_label.setText(self.current)  

       elif value == "%":  
           try:
               val = float(self.current)  
               val /= 100  
               self.current = str(val)  
               self.display_label.setText(self.current)  
           except:
               pass  

       elif value == "√":  
           try:
               val = float(self.current)  
               val = val ** 0.5  
               self.current = str(val)  
               self.display_label.setText(self.current)  
           except:
               pass  

if __name__ == "__main__": 
   app = QApplication(sys.argv) 
   calc = Calculator()  
   calc.show() 
   sys.exit(app.exec_()) 
