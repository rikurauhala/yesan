from entities.account import Account


class AccountRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, account):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO accounts (name, type) VALUES (?, ?)",
            (account.name, account.type)
        )
        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM accounts")

        rows = cursor.fetchall()

        return [Account(row["id"], row["name"], row["type"]) for row in rows]
