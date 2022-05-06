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

        self._account_a = Account(
            account_id=str(uuid.uuid4()),
            account_name="Name A",
            account_type="Type A"
        )

        self._account_repository.create(self._account_a)

        self._transaction_a = Transaction(
            transaction_id=str(uuid.uuid4()),
            date=date.today(),
            amount=-1000,
            category="Category A",
            description="Description A",
            account_id=self._account_a.id,
            party="Receiver A"
        )

        self._transaction_b = Transaction(
            transaction_id=str(uuid.uuid4()),
            date=date.today(),
            amount=-1000,
            category="Category B",
            description="Description B",
            account_id=self._account_a.id,
            party="Receiver B"
        )

    def test_create(self):
        success = self._transaction_repository.create(self._transaction_a)
        self.assertTrue(success)

    def test_cannot_reuse_same_uuid(self):
        success = self._transaction_repository.create(self._transaction_a)
        self.assertTrue(success)
        success = self._transaction_repository.create(self._transaction_a)
        self.assertFalse(success)

    def test_create_multiple(self):
        transactions = [self._transaction_a, self._transaction_a, self._transaction_b]
        created = self._transaction_repository.create_multiple(transactions)
        self.assertEqual(created, 2)

    def test_find_all(self):
        success = self._transaction_repository.create(self._transaction_a)
        self.assertTrue(success)
        transactions = self._transaction_repository.find_all()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].id, self._transaction_a.id)
        self.assertEqual(transactions[0].date, self._transaction_a.date.strftime("%Y-%m-%d"))
        self.assertEqual(transactions[0].amount, self._transaction_a.amount)
        self.assertEqual(transactions[0].category, self._transaction_a.category)
        self.assertEqual(transactions[0].description, self._transaction_a.description)
        self.assertEqual(transactions[0].account_id, self._account_a.name)
        self.assertEqual(transactions[0].party, self._transaction_a.party)

    def test_find_all_with_id(self):
        success = self._transaction_repository.create(self._transaction_a)
        self.assertTrue(success)
        transactions = self._transaction_repository.find_all_with_id()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].id, self._transaction_a.id)
        self.assertEqual(transactions[0].date, self._transaction_a.date.strftime("%Y-%m-%d"))
        self.assertEqual(transactions[0].amount, self._transaction_a.amount)
        self.assertEqual(transactions[0].category, self._transaction_a.category)
        self.assertEqual(transactions[0].description, self._transaction_a.description)
        self.assertEqual(transactions[0].account_id, self._transaction_a.account_id)
        self.assertEqual(transactions[0].party, self._transaction_a.party)

    def test_get_balance_by_id(self):
        success = self._transaction_repository.create(self._transaction_a)
        self.assertTrue(success)
        balance = self._transaction_repository.get_balance_by_id(self._account_a.id)
        self.assertEqual(balance, -1000)
        success = self._transaction_repository.create(self._transaction_b)
        self.assertTrue(success)
        balance = self._transaction_repository.get_balance_by_id(self._account_a.id)
        self.assertEqual(balance, -2000)

    def test_calculate_net_worth(self):
        success = self._transaction_repository.create(self._transaction_a)
        self.assertTrue(success)
        balance = self._transaction_repository.get_balance_by_id(self._account_a.id)
        self.assertEqual(balance, -1000)
        success = self._transaction_repository.create(self._transaction_b)
        self.assertTrue(success)
        net_worth = self._transaction_repository.calculate_net_worth()
        self.assertEqual(net_worth, -2000)
