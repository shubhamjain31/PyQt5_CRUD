import sys
from PyQt6.QtWidgets import QApplication

from contact_book.views import Window
from contact_book.database import createConnection

def main():

    """ main function."""

    # Create the application
    app = QApplication(sys.argv)

    # Connect to the database before creating any window
    if not createConnection("contacts.sqlite3"):
        sys.exit(1)

    # Create the main window
    win = Window()
    win.show()

    # Run the event loop
    sys.exit(app.exec())