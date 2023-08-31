import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget


def main():
    app = QApplication(sys.argv)

    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)

    tab_widget = QTabWidget()
    layout.addWidget(tab_widget)

    tab_widget.addTab(QWidget(), "Tab 1")
    tab_widget.addTab(QWidget(), "Tab 2")

    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
