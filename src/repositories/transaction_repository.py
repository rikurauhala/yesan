from sqlite3 import IntegrityError

from database import get_database_connection

from entities.transaction import Transaction


class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, transaction):
        try:
            cursor = self._connection.cursor()
            cursor.execute("""
                INSERT INTO transactions(
                    id, date, amount, category, 
                    description, account_id, party)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                           (transaction.id, transaction.date, transaction.amount,
                            transaction.category, transaction.description,
                            transaction.account_id, transaction.party))
            self._connection.commit()
            return True
        except IntegrityError:
            return False

    def create_multiple(self, transactions):
        created = 0
        for transaction in transactions:
            if self.create(transaction):
                created = created + 1
        return created

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT t.id, t.date, t.amount, t.category, t.description, a.name, t.party
            FROM transactions AS t, accounts AS a
            WHERE t.account_id = a.id
            ORDER BY t.date DESC
        """)

        rows = cursor.fetchall()

        transactions = []

        for row in rows:
            transaction_id = row["id"]
            date = row["date"]
            amount = row["amount"]
            category = row["category"]
            description = row["description"]
            account_name = row["name"]
            party = row["party"]
            transaction = Transaction(
                transaction_id, date, amount, category, description, account_name, party
            )
            transactions.append(transaction)

        return transactions

    def find_all_with_id(self):
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT id, date, amount, category, description, account_id, party
            FROM transactions
            ORDER BY date DESC
        """)

        rows = cursor.fetchall()

        transactions = []

        for row in rows:
            transaction_id = row["id"]
            date = row["date"]
            amount = row["amount"]
            category = row["category"]
            description = row["description"]
            account_id = row["account_id"]
            party = row["party"]
            transaction = Transaction(
                transaction_id, date, amount, category, description, account_id, party
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


transaction_repository = TransactionRepository(get_database_connection())
