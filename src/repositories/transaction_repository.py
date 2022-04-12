from entities.transaction import Transaction


class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, transaction):
        cursor = self._connection.cursor()
        cursor.execute("""
            INSERT INTO transactions(timestamp, amount, category, description, account_id, party)
            VALUES (?, ?, ?, ?, ?, ?)""",
                       (transaction.timestamp, transaction.amount, transaction.category,
                        transaction.description, transaction.account_id, transaction.party)
                       )
        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT t.id, t.timestamp, t.amount, t.category, t.description, a.name, t.party
            FROM transactions AS t, accounts AS a
            WHERE t.account_id = a.id
            ORDER BY t.timestamp DESC
        """)

        rows = cursor.fetchall()

        transactions = []

        for row in rows:
            timestamp = row["timestamp"]
            amount = row["amount"]
            category = row["category"]
            description = row["description"]
            account_name = row["name"]
            party = row["party"]
            transaction = Transaction(
                timestamp, amount, category, description, account_name, party
            )
            transactions.append(transaction)

        return transactions
