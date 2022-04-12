from database.database_operations import get_database_connection
from entities.transaction import Transaction
from repositories.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self):
        self._transaction_repository = TransactionRepository(
            get_database_connection()
        )

    def create_transaction(self, date, amount, category, description, account_id, party):
        new_transaction = Transaction(
            date,
            amount,
            category,
            description,
            account_id,
            party
        )
        return self._transaction_repository.create(new_transaction)

    def find_all(self):
        return self._transaction_repository.find_all()
