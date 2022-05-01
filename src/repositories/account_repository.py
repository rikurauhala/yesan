from sqlite3 import IntegrityError

from database import get_database_connection

from entities.account import Account


class AccountRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, account):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO accounts (id, name, type) VALUES (?, ?, ?)",
            (account.id, account.name, account.type)
        )
        self._connection.commit()
        return True

    def create_multiple(self, accounts):
        try:
            cursor = self._connection.cursor()
            cursor.executemany(
                "INSERT INTO accounts (id, name, type) VALUES (?, ?, ?)",
                accounts
            )
            self._connection.commit()
            return True
        except IntegrityError:
            return False

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM accounts ORDER BY name")
        rows = cursor.fetchall()
        return [Account(row["id"], row["name"], row["type"]) for row in rows]

    def get_list(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT name FROM accounts ORDER BY name")
        rows = cursor.fetchall()
        return [row["name"] for row in rows]

    def get_id_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id FROM accounts WHERE name=(?)", (name, ))
        return cursor.fetchone()[0]

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM accounts")
        self._connection.commit()


account_repository = AccountRepository(get_database_connection())
