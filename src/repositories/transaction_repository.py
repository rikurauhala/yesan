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
            transaction_id = row["id"]
            timestamp = row["timestamp"]
            amount = row["amount"]
            category = row["category"]
            description = row["description"]
            account_id = row["account_id"]
            party = row["party"]

            transaction = Transaction(
                transaction_id, timestamp, amount, category, description, account_id, party
            )

            transactions.append(transaction)

        return transactions
