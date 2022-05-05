import uuid

import re

from file_handler import file_handler

from entities.transaction import Transaction

from repositories.transaction_repository import transaction_repository


class TransactionService:
    """Handles all functionality related to transactions."""

    def __init__(self):
        """Initializes a new instance of TransactionService."""
        self._transaction_repository = transaction_repository

    def _convert_to_int(self, amount):
        if re.match(r"^(\+|-)?\d+$", amount):
            return int(amount + "00")
        euro = amount.split(".")[0]
        cents = amount.split(".")[1]

        if len(cents) == 1:
            cents = cents + "0"

        return int(euro + cents)

    def create_transaction(self, date, amount, category, description, account_id, party):
        """Creates a new transaction.

        Args:
            date (Timestamp): Date when the transaction was made.
            amount (Integer): Amount of money involved in the transaction.
            category (String): String, category to which the transaction belongs to.
            description (String): Describes the purpose of the transaction.
            account_id (String): Connects the transaction to an account.
            party (String): Specifies the other party (payer/receiver) of the transaction.

        Returns:
            Boolean: True or false depending on if creation succeeded or not.
        """
        transaction_id = str(uuid.uuid4())
        amount = self._convert_to_int(amount)
        transaction = Transaction(
            transaction_id,
            date,
            amount,
            category,
            description,
            account_id,
            party
        )
        return self._transaction_repository.create(transaction)

    def find_all(self):
        """Finds all transactions.

        Returns:
            List containing all transaction data as Transaction objects.
        """
        return self._transaction_repository.find_all()

    def format_amount(self, amount):
        """Formats the given amount in a more readable form.

        Args:
            amount (Integer): Amount to be formatted.

        Returns:
            String: Formatted amount.
        """
        currency = f"{amount/100:,.2f} €"
        euros = currency.split(".")[0]
        cents = currency.split(".")[1]
        euros = euros.replace(",", " ")
        currency = f"{euros}.{cents}"
        return currency

    def find_all_as_list(self):
        """Finds all transactions in a list form.

        Returns:
            List of transactions details as list.
        """
        transactions = self._transaction_repository.find_all()
        transaction_list = []
        for transaction in transactions:
            details = []
            details.append(transaction.date)
            details.append(self.format_amount(transaction.amount))
            details.append(transaction.category)
            details.append(transaction.description)
            details.append(transaction.account_id)
            details.append(transaction.party)
            transaction_list.append(details)
        return transaction_list

    def find_all_with_id(self):
        """Finds all transactions including account id instead of account name.

        Returns:
            List containing all transaction data as Transaction objects.
        """
        return self._transaction_repository.find_all_with_id()

    def get_balance_by_id(self, account_id):
        """Returns the account balance based on its id.

        Args:
            account_id (String): Unique identifier of an account.

        Returns:
            Integer: Account balance.
        """
        return self._transaction_repository.get_balance_by_id(account_id)

    def calculate_net_worth(self):
        """Calculates the net worth (total balance of all accounts).

        Returns:
            Integer: Net worth.
        """
        return self._transaction_repository.calculate_net_worth()

    def delete_all(self):
        """Deletes all transaction data.

        Returns:
            Boolean: True after the operation succeeds as expected.
        """
        return self._transaction_repository.delete_all()

    def import_transactions(self):
        """Imports transaction data from a csv file.

        Returns:
            Integer: Number of transactions imported.
        """
        transactions = file_handler.import_transactions()
        return self._transaction_repository.create_multiple(transactions)

    def export_transactions(self):
        """Exports transaction data into a csv file.

        Returns:
            Boolean: True if exporting transactions succeeded.
        """
        transactions = self.find_all_with_id()
        return file_handler.export_transactions(transactions)
