from entities.account import Account


class AccountRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM accounts")

        rows = cursor.fetchall()

        return [Account(row["id"], row["name"], row["type"]) for row in rows]
