import uuid

from entities.account import Account


class AccountRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, account_name, account_type):
        account_id = str(uuid.uuid4())
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO accounts (id, name, type) VALUES (?, ?, ?)",
            (account_id, account_name, account_type)
        )
        self._connection.commit()
        return True

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
