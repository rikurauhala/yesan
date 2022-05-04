from sqlite3 import IntegrityError

from database import get_database_connection

from entities.transaction import Transaction


class TransactionRepository:
    """Handles all database operations related to transactions."""

    def __init__(self, connection):
        """Initializes a new instance of TransactionRepository.

        Args:
            connection (Connection object): Connection to the database.
        """
        self._connection = connection

    def create(self, transaction):
        """Inserts a new transaction into the database.

        Args:
            transaction (Transaction): Transaction object.

        Returns:
            Boolean: True or False depending on if creation succeeded or not.
        """
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
        """Inserts multiple transactions in to the database.

        Args:
            transactions (List): List of Transaction objects.

        Returns:
            Integer: Number of transactions created.
        """
        created = 0
        for transaction in transactions:
            if self.create(transaction):
                created = created + 1
        return created

    def find_all(self):
        """Finds all transaction data from the database.

        Returns:
            List of Transaction objects.
        """
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
        """Finds all transactions including account id instead of account name.

        Returns:
            List of Transaction objects.
        """

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
        """_Deletes all transaction data from the database.

        Returns:
            Boolean: True or False depending on if deletion succeeded or not.
        """
        try:
            cursor = self._connection.cursor()
            cursor.execute("DELETE FROM transactions")
            self._connection.commit()
            return True
        except Exception:
            return False

    def get_balance_by_id(self, account_id):
        """Calculates the account balance based on its id.

        Args:
            account_id (String): Unique identifier of an account.

        Returns:
            Integer: Account balance.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT SUM(amount) FROM transactions WHERE account_id=(?)", (account_id, ))
        return cursor.fetchone()[0]

    def calculate_net_worth(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT SUM(amount) FROM transactions")
        return cursor.fetchone()[0]


transaction_repository = TransactionRepository(get_database_connection())
