import csv

from config import TRANSACTIONS_FILE_PATH

from database_operations import get_database_connection

from entities.transaction import Transaction

from repositories.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self):
        self._transaction_repository = TransactionRepository(
            get_database_connection()
        )

    def _convert_to_int(self, amount):
        euro = amount.split(".")[0]
        cents = amount.split(".")[1]

        if len(cents) == 1:
            cents = cents + "0"

        return int(euro + cents)

    def create_transaction(self, date, amount, category, description, account_id, party):
        amount = self._convert_to_int(amount)
        return self._transaction_repository.create(
            date, amount, category,
            description, account_id, party
        )

    def find_all(self):
        return self._transaction_repository.find_all()

    def find_all_with_id(self):
        return self._transaction_repository.find_all_with_id()

    def get_balance_by_id(self, account_id):
        return self._transaction_repository.get_balance_by_id(account_id)

    def export(self):
        transactions = self.find_all_with_id()

        with open(TRANSACTIONS_FILE_PATH, "w", encoding="UTF8") as file:
            writer = csv.writer(file)
            for transaction in transactions:
                details = []
                details.append(transaction.timestamp)
                details.append(transaction.amount)
                details.append(transaction.category)
                details.append(transaction.description)
                details.append(transaction.account_id)
                details.append(transaction.party)
                writer.writerow(details)

        return True
