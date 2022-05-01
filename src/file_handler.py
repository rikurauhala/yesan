import csv

from config import ACCOUNTS_FILE_PATH
from config import TRANSACTIONS_FILE_PATH

from entities.account import Account
from entities.transaction import Transaction


class FileHandler:

    def __init__(self):
        pass

    def import_accounts(self):
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
