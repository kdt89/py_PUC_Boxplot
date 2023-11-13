import sys
from PyQt6.QtWidgets import QApplication
from mvc_view import UI
from mvc_controller import Controller
from mvc_model import Model


'''
Main Program
'''
if __name__ == "__main__":

    # UI intialize
    app = QApplication(sys.argv)
    # generate main View object
    view = UI()
    # generate main program data Model
    model = Model()
    # Let Controller setup the Logic flow
    mainController = Controller(model=model, view=view)

    sys.exit(app.exec())  # loop in ui event
