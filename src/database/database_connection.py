import os
import sqlite3

dirname = os.path.dirname(__file__)
os.makedirs(os.path.join(dirname, "..", "data"), exist_ok=True)

connection = sqlite3.connect(os.path.join(
    dirname, "..", "data", "database.sqlite"),
    detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
