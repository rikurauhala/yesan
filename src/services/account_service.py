import uuid

from file_handler import file_handler

from entities.account import Account

from repositories.account_repository import account_repository


class AccountService:
    """Handles all functionality related to accounts."""

    def __init__(self):
        """Initializes a new instance of AccountService."""
        self._account_repository = account_repository

    def create_account(self, account_name, account_type):
        """Creates a new account.

        Args:
            account_name (String): Name of the account.
            account_type (String): Type of the account.

        Returns:
            Boolean: True or False depending if creation succeeded or not.
        """

        account_uuid = str(uuid.uuid4())
        account = Account(
            account_uuid,
            account_name,
            account_type
        )
        return self._account_repository.create(account)

    def find_all(self):
        """Finds all accounts.

        Returns:
            List containing all account data as Account objects.
        """
        return self._account_repository.find_all()

    def get_list(self):
        """Finds a list of account names in alphabetical order.

        Returns:
            List of account names in alphabetical order.
        """
        return self._account_repository.get_list()

    def get_id_by_name(self, name):
        """Finds the id of an account by its name.

        Args:
            name (String): Name of the account to be found.

        Returns:
            String: Id of the account in the UUID format.
        """
        return self._account_repository.get_id_by_name(name)

    def delete_all(self):
        """Deletes all account data.

        Returns:
            Boolean: True or False depending if deletion succeeded or not.
        """
        return self._account_repository.delete_all()

    def import_accounts(self):
        """Imports account data from a csv file.

        Returns:
            Integer: Number of accounts imported.
        """
        accounts = file_handler.import_accounts()
        return self._account_repository.create_multiple(accounts)

    def export_accounts(self):
        """Exports account data into a csv file.

        Returns:
            Boolean: True if exporting accounts succeeded.
        """
        accounts = self.find_all()
        return file_handler.export_accounts(accounts)
