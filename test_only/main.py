from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication
import sys


app = QApplication(sys.argv)

window = QWidget()        
button1 = QPushButton("One")        
button2 = QPushButton("Two")
button3 = QPushButton("Three")
button4 = QPushButton("Four")
button5 = QPushButton("Five")

# layout = QGridLayout(window)        

layout = QGridLayout()
window.setLayout(layout)
layout.addWidget(button1, 0, 0)
layout.addWidget(button2, 0, 1)
layout.addWidget(button3, 1, 0, 1, 2)
layout.addWidget(button4, 2, 0)
layout.addWidget(button5, 2, 1)        



window.show()
sys.exit(app.exec())