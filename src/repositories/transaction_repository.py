import uuid

from entities.transaction import Transaction


class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, date, amount, category, description, account_id, party):
        cursor = self._connection.cursor()
        transaction_id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO transactions(
                id, timestamp, amount, category, 
                description, account_id, party)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
                       (transaction_id, date, amount, category, description, account_id, party))
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
            transaction_id = row["id"]
            timestamp = row["timestamp"]
            amount = row["amount"]
            category = row["category"]
            description = row["description"]
            account_name = row["name"]
            party = row["party"]
            transaction = Transaction(
                transaction_id, timestamp, amount, category, description, account_name, party
            )
            transactions.append(transaction)

        return transactions

    def find_all_with_id(self):
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT id, timestamp, amount, category, description, account_id, party
            FROM transactions
            ORDER BY timestamp DESC
        """)

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

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM transactions")
        self._connection.commit()

    def get_balance_by_id(self, account_id):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT SUM(amount) FROM transactions WHERE account_id=(?)", (account_id, ))
        return cursor.fetchone()[0]
