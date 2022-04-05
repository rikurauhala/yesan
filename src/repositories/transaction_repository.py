from entities.transaction import Transaction


class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM transactions")

        rows = cursor.fetchall()

        transactions = []

        for row in rows:
            transaction = Transaction()
            transaction.id = row["id"]
            transaction.timestamp = row["timestamp"]
            transaction.amount = row["amount"]
            transaction.category = row["category"]
            transaction.description = row["description"]
            transaction.account_id = row["account_id"]
            transaction.party = row["party"]
            transactions.append(transaction)

        return transactions
