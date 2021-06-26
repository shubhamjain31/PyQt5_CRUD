from database import createConnection
import os

# Create a connection

file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "contacts.sqlite3")
createConnection(file)

# Confirm that contacts table exists
from PyQt5.QtSql import QSqlDatabase
db = QSqlDatabase.database()
print(db.tables())
db.tables()