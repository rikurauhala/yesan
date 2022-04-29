import os
import sqlite3

from config import DATABASE_FILE_PATH


dirname = os.path.dirname(__file__)
os.makedirs(os.path.join(dirname, "..", "data"), exist_ok=True)

database_connection = sqlite3.connect(
    DATABASE_FILE_PATH,
    detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
)
database_connection.row_factory = sqlite3.Row


def get_database_connection():
    return database_connection


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
            id TEXT PRIMARY KEY,
            name TEXT,
            type TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE transactions (
            id TEXT PRIMARY KEY,
            date INTEGER,
            amount INTEGER,
            category TEXT,
            description TEXT,
            account_id TEXT REFERENCES accounts,
            party TEXT
        );
    """)

    connection.commit()

    print("Database initialized")


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
