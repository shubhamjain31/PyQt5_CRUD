import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql


class showWindow(QtWidgets.QStyledItemDelegate):
    def displayText(self, value, locale):
        if isinstance(value, QtCore.QByteArray):
            value = value.data().decode()
        return super(showWindow, self).displayText(value, locale)


def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pyqt5.sqlite3")
    db.setDatabaseName(file)
    if not db.open():
        QtWidgets.QMessageBox.critical(
            None,
            QtWidgets.qApp.tr("Cannot open database"),
            QtWidgets.qApp.tr(
                "Unable to establish a database connection.\n"
                "This example needs SQLite support. Please read "
                "the Qt SQL driver documentation for information "
                "how to build it.\n\n"
                "Click Cancel to exit."
            ),
            QtWidgets.QMessageBox.Cancel,
        )
        return False
    return True


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    if not createConnection():
        sys.exit(-1)

    window = QtWidgets.QTableView()
    window.horizontalHeader().setStretchLastSection(True)
    window.setWordWrap(True)
    window.setTextElideMode(QtCore.Qt.ElideLeft)
    delegate = showWindow(window)
    window.setItemDelegateForColumn(4, delegate)
    model = QtSql.QSqlQueryModel()
    model.setQuery("SELECT * FROM employee")
    window.setModel(model)
    window.resize(640, 480)
    window.show()

    sys.exit(app.exec_())
