import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class VerticalTabWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vertical Tab Widget Example")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        tab_widget = QTabWidget()

        # Set the tab bar to be oriented vertically
        tab_bar = tab_widget.tabBar()
        tab_bar.setOrientation(Qt.Vertical)

        # Create tabs and add them to the tab widget
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")
        tab_widget.addTab(tab3, "Tab 3")

        # Add content to the tabs
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("Content of Tab 1"))
        tab1.setLayout(tab1_layout)

        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("Content of Tab 2"))
        tab2.setLayout(tab2_layout)

        tab3_layout = QVBoxLayout()
        tab3_layout.addWidget(QLabel("Content of Tab 3"))
        tab3.setLayout(tab3_layout)

        layout.addWidget(tab_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VerticalTabWidget()
    window.show()
    sys.exit(app.exec())
