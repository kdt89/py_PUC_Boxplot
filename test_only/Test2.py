import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QTabWidget
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

app = QApplication(sys.argv)

# Create the main widget
main_widget = QMainWindow()
main_widget.setWindowTitle("Matplotlib Figure Resize Example")

# Create the figure and canvas
fig = Figure()
canvas = FigureCanvas(fig)

# Create a subplot and plot a simple curve
ax = fig.add_subplot(111)
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
ax.plot(x, y)

# Create the layout for the main widget
layout = QVBoxLayout()
main_widget.setLayout(layout)

# Create the form layout
form_layout = QFormLayout()
layout.addLayout(form_layout)

# Create the tab widget
tab_widget = QTabWidget()
form_layout.addRow(tab_widget)

# Add the canvas to the tab widget
tab_widget.addTab(canvas, "Figure")

# Function to handle resizing of the main widget
def resize_event(event):
    # Update the figure's layout to fit within the available space
    fig.tight_layout()
    canvas.draw()




# Connect the resize event of the main widget to the resize_event function
main_widget.resizeEvent = resize_event

# Show the main widget
main_widget.show()



sys.exit(app.exec())