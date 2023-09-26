# importing various libraries
import sys
from PyQt6.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random

# main window
# which inherits QDialog
class Window(QWidget):
	
	# constructor
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)

		# a figure instance to plot on
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		
		# adding canvas to the layout
		layout = QVBoxLayout()
		layout.addWidget(self.canvas)
		# setting layout to the main window
		self.setLayout(layout)

		# random data
		data = [random.random() for i in range(10)]
		# clearing old figure
		self.figure.clear()
		# create an axis
		ax = self.figure.add_subplot(111)
		# plot data
		ax.plot(data, '*-')
		# refresh canvas
		self.canvas.draw()

# driver code
if __name__ == '__main__':
	
	# creating apyqt5 application
	app = QApplication(sys.argv)

	# creating a window object
	window1 = Window()
	window2 = Window()

	# showing the window
	window1.show()
	window2.show()

	# loop
	sys.exit(app.exec())
