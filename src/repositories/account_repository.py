from sqlite3 import IntegrityError

from database import get_database_connection

from entities.account import Account


class AccountRepository:
    """Handles all database operations related to accounts."""

    def __init__(self, connection):
        """Initializes a new instance of AccountRepository."""
        self._connection = connection

    def create(self, account):
        """Inserts a new account into the database.

        Args:
            account (Account): Account object.

        Returns:
            Boolean: True or False depending on if creation succeeded or not.
        """
        try:
            cursor = self._connection.cursor()
            cursor.execute(
                "INSERT INTO accounts (id, name, type) VALUES (?, ?, ?)",
                (account.id, account.name, account.type)
            )
            self._connection.commit()
            return True
        except IntegrityError:
            return False

    def create_multiple(self, accounts):
        """Inserts multiple accounts in to the database.

        Args:
            accounts (List): List of Account objects.

        Returns:
            Integer: Number of accounts created.
        """
        created = 0
        for account in accounts:
            if self.create(account):
                created = created + 1
        return created

    def find_all(self):
        """Finds all account data from the database.

        Returns:
            List of Account objects.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM accounts ORDER BY name")
        rows = cursor.fetchall()
        return [Account(row["id"], row["name"], row["type"]) for row in rows]

    def get_list(self):
        """Finds the names of all accounts from the database.

        Returns:
            List of account names.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT name FROM accounts ORDER BY name")
        rows = cursor.fetchall()
        return [row["name"] for row in rows]

    def get_id_by_name(self, name):
        """Finds the unique identifier of a given account based on its name.

        Args:
            name (String): Name of the account to be found.

        Returns:
            String: Id of the account in the UUID format.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT id FROM accounts WHERE name=(?)", (name, ))
        return cursor.fetchone()[0]

    def delete_all(self):
        """Deletes all account data from the database.

        Returns:
            Boolean: True or False depending on if deletion succeeded or not.
        """
        try:
            cursor = self._connection.cursor()
            cursor.execute("DELETE FROM accounts")
            self._connection.commit()
            return True
        except Exception:
            return False


account_repository = AccountRepository(get_database_connection())
