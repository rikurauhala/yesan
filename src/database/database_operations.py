import subprocess

from database_connection import get_database_connection


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

def create_database_file():
    subprocess.call(["sh", "./init.sh"])

def initialize_database():
    connection = get_database_connection()
    create_database_file()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
