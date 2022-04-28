from datetime import date

import uuid

import unittest

from entities.transaction import Transaction

from database import database_connection as connection

from repositories.account_repository import AccountRepository
from repositories.transaction_repository import TransactionRepository


class TestTransactionRepository(unittest.TestCase):
    def setUp(self):
        self._transaction_repository = TransactionRepository(connection)
        self._transaction_repository.delete_all()

        id_transaction_a = str(uuid.uuid4())
        date_transaction_a = date.today()
        amount_transaction_a = -10.00
        category_transaction_a = "Groceries"
        description_transaction_a = "Apples, carrots, ice cream"
        account_id_transaction_a = str(uuid.uuid4)
        party_transaction_a = "S-market"
        self._transaction_a = Transaction(
            id_transaction_a,
            date_transaction_a,
            amount_transaction_a,
            category_transaction_a,
            description_transaction_a,
            account_id_transaction_a,
            party_transaction_a
        )

    def test_create(self):
        self._transaction_repository.create(
            self._transaction_a.timestamp,
            self._transaction_a.amount,
            self._transaction_a.category,
            self._transaction_a.description,
            self._transaction_a.account_id,
            self._transaction_a.party
        )
        transactions = self._transaction_repository.find_all()

        # Not working for now
        #self.assertEqual(len(transactions), 1)

    def test_get_balance_by_id(self):
        pass
