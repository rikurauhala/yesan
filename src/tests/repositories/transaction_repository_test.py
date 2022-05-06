from datetime import date

import uuid

import unittest

from database import database_connection as connection

from entities.account import Account
from entities.transaction import Transaction

from repositories.account_repository import AccountRepository
from repositories.transaction_repository import TransactionRepository


class TestTransactionRepository(unittest.TestCase):
    def setUp(self):
        self._transaction_repository = TransactionRepository(connection)
        self._transaction_repository.delete_all()
        self._account_repository = AccountRepository(connection)
        self._account_repository.delete_all()

        self._uuid_account_a = str(uuid.uuid4())
        self._name_account_a = "Name A"
        self._type_account_a = "Type A"
        self._account_a = Account(
            self._uuid_account_a,
            self._name_account_a,
            self._type_account_a
        )

        self._account_repository.create(self._account_a)

        id_transaction_a = str(uuid.uuid4())
        date_transaction_a = date.today()
        amount_transaction_a = -1000
        category_transaction_a = "Category A"
        description_transaction_a = "Description A"
        account_id_transaction_a = self._uuid_account_a
        party_transaction_a = "Receiver A"
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
        success = self._transaction_repository.create(self._transaction_a)
        self.assertTrue(success)

    def test_find_all(self):
        success = self._transaction_repository.create(self._transaction_a)
        self.assertTrue(success)
        transactions = self._transaction_repository.find_all()
        print(transactions)
        self.assertEqual(len(transactions), 1)

    def test_cannot_reuse_uuid(self):
        success = self._transaction_repository.create(self._transaction_a)
        self.assertTrue(success)
        success = self._transaction_repository.create(self._transaction_a)
        self.assertFalse(success)
