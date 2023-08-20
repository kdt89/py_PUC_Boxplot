import sys
import mvc_view
import mvc_controller
import mvc_model
from PyQt6.QtWidgets import QApplication


'''
Main Program
'''
if __name__ == "__main__":

    # UI intialize
    app = QApplication(sys.argv)

    # generate main View object
    view= mvc_view.UI()

    # generate main program data Model
    model = mvc_model.Model()
    # Let Controller setup the Logic flow
    mainController = mvc_controller.Controller(model=model, view=view)

    sys.exit(app.exec()) # loop in ui event


