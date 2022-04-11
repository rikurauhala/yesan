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


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS accounts;
    """)

    cursor.execute("""
        DROP TABLE IF EXISTS transactions;
    """)

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE transactions (
            id INTEGER PRIMARY KEY,
            timestamp INTEGER,
            amount INTEGER,
            category TEXT,
            description TEXT,
            account_id INTEGER REFERENCES accounts,
            party TEXT
        );
    """)

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
