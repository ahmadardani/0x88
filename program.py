import sys
from PySide6 import QtWidgets # Import the necessary Qt modules

# Import the UI definition from the generated file
# Make sure 'Ui_MainWindow' matches the class name in your ui_program.py
from programui_ui import Ui_MainWindow

class MyProgram(QtWidgets.QMainWindow): # Your main window class
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI
        self.ui = Ui_MainWindow()
        # Set up the UI on this QMainWindow instance
        self.ui.setupUi(self)

        # --- Connect your widgets to functions here ---
        # For example, if you have a QPushButton named 'pushButton' in Designer:
        # self.ui.pushButton.clicked.connect(self.my_button_clicked)

        # If you have a QLabel named 'label':
        # self.ui.label.setText("Welcome to my app!")

    # --- Define your widget interaction functions here ---
    # def my_button_clicked(self):
    #     print("Button was clicked!")
    #     self.ui.label.setText("Button clicked!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create the application instance
    window = MyProgram()                   # Create an instance of your main window
    window.show()                          # Show the window
    sys.exit(app.exec())                   # Start the event loop