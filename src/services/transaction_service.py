import uuid

from file_handler import file_handler

from entities.transaction import Transaction

from repositories.transaction_repository import transaction_repository


class TransactionService:
    def __init__(self):
        self._transaction_repository = transaction_repository

    def _convert_to_int(self, amount):
        euro = amount.split(".")[0]
        cents = amount.split(".")[1]

        if len(cents) == 1:
            cents = cents + "0"

        return int(euro + cents)

    def create_transaction(self, date, amount, category, description, account_id, party):
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
        return self._transaction_repository.find_all()

    def find_all_with_id(self):
        return self._transaction_repository.find_all_with_id()

    def get_balance_by_id(self, account_id):
        return self._transaction_repository.get_balance_by_id(account_id)

    def import_transactions(self):
        transactions = file_handler.import_transactions()
        return self._transaction_repository.create_multiple(transactions)

    def export_transactions(self):
        transactions = self.find_all_with_id()
        return file_handler.export_transactions(transactions)
