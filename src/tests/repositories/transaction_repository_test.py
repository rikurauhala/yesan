from datetime import date

import unittest

from entities.transaction import Transaction

from database_operations import database_connection as connection

from repositories.transaction_repository import TransactionRepository


class TestTransactionRepository(unittest.TestCase):
    def setUp(self):
        self._transaction_repository = TransactionRepository(connection)
        self._transaction_repository.delete_all()

    def test_create(self):
        date_transaction_a = date.today()
        amount_transaction_a = -10.00
        category_transaction_a = "Groceries"
        description_transaction_a = "Apples, carrots, ice cream"
        account_id_transaction_a = 1
        party_transaction_a = "S-market"
        self._transaction_a = Transaction(
            date_transaction_a,
            amount_transaction_a,
            category_transaction_a,
            description_transaction_a,
            account_id_transaction_a,
            party_transaction_a
        )

        self._transaction_repository.create(self._transaction_a)
        transactions = self._transaction_repository.find_all()

        self.assertEqual(len(transactions), 1)
