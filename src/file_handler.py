import csv

from config import ACCOUNTS_FILE_PATH
from config import TRANSACTIONS_FILE_PATH


class FileHandler:

    def __init__(self):
        pass

    def import_accounts(self):
        pass

    def export_accounts(self, accounts):
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
        pass

    def export_transactions(self, transactions):
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


file_handler = FileHandler()
