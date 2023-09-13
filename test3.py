import matplotlib.pyplot as plt
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

app = QApplication([])

# Create two Matplotlib Figure objects
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data on the first figure
ax1.plot(x, y)

# Plot the data on the second figure
ax2.plot(x, -y)

# Create FigureCanvasQTAgg objects for each figure
canvas1 = FigureCanvasQTAgg(fig1)
canvas2 = FigureCanvasQTAgg(fig2)

# Add the FigureCanvasQTAgg objects to a layout
layout = QVBoxLayout()
layout.addWidget(canvas1)
layout.addWidget(canvas2)

# Create a PyQt6 widget
widget = QWidget()
widget.setLayout(layout)

# Show the widget
widget.show()

app.exec()