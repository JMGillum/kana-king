from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.words = ["hello","hola","hallo","bonjour","konnichiwa"]
        self.setWindowTitle("Kana King")
        self.button = QPushButton("PRESS ME!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)
    
    
    def the_button_was_clicked(self):
        self.setWindowTitle(choice(self.words))
    
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)
    
    def the_window_title_changed(self,window_title):
        print(f"Window title changed: {window_title}")

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.