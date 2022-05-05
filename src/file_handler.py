import csv
import os

from config import ACCOUNTS_FILE_PATH
from config import TRANSACTIONS_FILE_PATH

from entities.account import Account
from entities.transaction import Transaction


class FileHandler:
    """Handles all functionality related to reading from or writing to a file."""

    def __init__(self):
        """Initializes a new instance of FileHandler."""
        dirname = os.path.dirname(__file__)
        root_folder = os.path.join(dirname, "..")
        self._env_file = os.path.join(root_folder, ".env")

    def import_accounts(self):
        """Imports account data from a csv file.

        Returns:
            List of Account objects.
        """
        accounts = []
        with open(ACCOUNTS_FILE_PATH, "r", encoding="UTF8") as file:
            reader = csv.reader(file)
            for row in reader:
                account_uuid = row[0]
                account_name = row[1]
                account_type = row[2]
                account = Account(
                    account_uuid,
                    account_name,
                    account_type
                )
                accounts.append(account)
        return accounts

    def export_accounts(self, accounts):
        """Exports account data into a csv file.

        Args:
            accounts (List): List of Account objects.

        Returns:
            Boolean: True if exporting succeeds.
        """
        with open(ACCOUNTS_FILE_PATH, "w", encoding="UTF8") as file:
            writer = csv.writer(file)
            for account in accounts:
                details = []
                details.append(account.id)
                details.append(account.name)
                details.append(account.type)
                writer.writerow(details)
        return True

    def import_transactions(self):
        """Imports transaction data from a csv file.

        Returns:
            List of Transaction objects.
        """
        transactions = []
        with open(TRANSACTIONS_FILE_PATH, "r", encoding="UTF8") as file:
            reader = csv.reader(file)
            for row in reader:
                transaction_id = row[0]
                transaction_date = row[1]
                transaction_amount = row[2]
                transaction_category = row[3]
                transaction_description = row[4]
                transaction_account_id = row[5]
                transaction_party = row[6]
                transaction = Transaction(
                    transaction_id,
                    transaction_date,
                    transaction_amount,
                    transaction_category,
                    transaction_description,
                    transaction_account_id,
                    transaction_party,
                )
                transactions.append(transaction)
        return transactions

    def export_transactions(self, transactions):
        """Exports transaction data into a csv file.

        Args:
            transactions (List): List of Transaction objects.

        Returns:
            Boolean: True if exporting succeeds.
        """
        with open(TRANSACTIONS_FILE_PATH, "w", encoding="UTF8") as file:
            writer = csv.writer(file)
            for transaction in transactions:
                details = []
                details.append(transaction.id)
                details.append(transaction.date)
                details.append(transaction.amount)
                details.append(transaction.category)
                details.append(transaction.description)
                details.append(transaction.account_id)
                details.append(transaction.party)
                writer.writerow(details)
        return True

    def import_settings(self):
        """Imports settings from the .env file.

        Returns:
            List: Rows containing the contents of the env. file.
        """
        config_lines = []
        with open(self._env_file, "r", encoding="UTF8") as file:
            lines = file.readlines()
            for line in lines:
                config_lines.append(line)
        return config_lines

    def export_settings(self, content):
        """Exports settings into the .env file.

        Args:
            content (List): Rows containin the contents of the Text object in the Settings view.

        Returns:
            Boolean: True if the operation succeeded as expected.
        """
        with open(self._env_file, "w", encoding="UTF8") as file:
            file.writelines(content)
        return True


file_handler = FileHandler()
