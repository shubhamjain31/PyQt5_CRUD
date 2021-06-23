# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys

import sqlite3

conn = sqlite3.connect('pyqt5.sqlite3')
print("Opened database successfully",conn)


# creating a class
# that inherits the QDialog class
class addWindow(QDialog):

    # constructor
    def __init__(self):
        super(addWindow, self).__init__()

        # setting window title
        self.setWindowTitle("Show")

        # setting geometry to the window(left, top, width, height)
        self.setGeometry(700, 300, 400, 500)

        # changing the background color to yellow
        # self.setStyleSheet("background-color: lightblue;")

        # creating a group box
        self.formGroupBox = QGroupBox("")

        # creating spin box to select age
        self.ageSpinBar = QSpinBox(width=5)

        # creating combo box to select degree
        self.degreeComboBox = QComboBox()

        # adding items to the combo box
        self.degreeComboBox.addItems(["BTech", "MTech", "PhD"])

        # creating a line edit
        self.nameLineEdit = QLineEdit()
        # self.nameLineEdit.setFixedWidth(120)
        # self.nameLineEdit.setFixedHeight(12)

        # creating a line edit
        self.countryLineEdit = QLineEdit()
        self.countryLineEdit.setGeometry(QtCore.QRect(0,0,400,700))

        # calling the method that create the form
        self.createForm()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)

        # addding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting lay out
        self.setLayout(mainLayout)

        # full screen
        # self.showMaximized()

    # get info method called when form is accepted
    def getInfo(self):
        try:
            name    = self.nameLineEdit.text()
            course  = self.degreeComboBox.currentText()
            age     = self.ageSpinBar.text()
            country = self.countryLineEdit.text()
            
            conn.execute("insert into employee (name, course, country, age) values (?, ?, ?, ?)",
            (name, course, country, age))
            conn.commit()
            QMessageBox.about(self, 'Connection', 'Record created successfully !')
            conn.close()
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database !')
            sys.exit(1)


        # printing the form information
        print("Person Name : {0}".format(self.nameLineEdit.text()))
        print("Degree : {0}".format(self.degreeComboBox.currentText()))
        print("Age : {0}".format(self.ageSpinBar.text()))

        # closing the window
        self.close()

    # creat form method
    def createForm(self):

        # creating a form layout
        layout = QFormLayout()

        # adding rows
        # for name and adding input text
        self.nameLabel = QLabel("Name")
        self.nameLabel.setStyleSheet("background-color: lightblue;")
        layout.addRow(self.nameLabel, self.nameLineEdit)

        # for degree and adding combo box
        self.courseLabel = QLabel("Course")
        layout.addRow(self.courseLabel, self.degreeComboBox)

        # for age and adding spin box
        self.ageLabel = QLabel("Age")
        layout.addRow(self.ageLabel, self.ageSpinBar)

        self.countryLabel = QLabel("Country")
        layout.addRow(self.countryLabel, self.countryLineEdit)

        # setting layout
        self.formGroupBox.setLayout(layout)


# main method
if __name__ == '__main__':

    # create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = addWindow()

    # showing the window
    window.show()

    # start the app
    sys.exit(app.exec())
