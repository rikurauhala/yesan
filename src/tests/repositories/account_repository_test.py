import unittest

from entities.account import Account

from database.database_operations import database_connection

from repositories.account_repository import AccountRepository


class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        self._account_repository = AccountRepository(database_connection)
        self._account_repository.delete_all()

        name_account_a = "Checking account"
        type_account_a = "Bank account"
        self._account_a = Account(None, name_account_a, type_account_a)

        name_account_b = "Bitcoin"
        type_account_b = "Crypto currency"
        self._account_b = Account(None, name_account_b, type_account_b)

    def test_create(self):
        self._account_repository.create(self._account_b)
        accounts = self._account_repository.find_all()

        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].id, 1)
        self.assertEqual(accounts[0].name, self._account_b.name)
        self.assertEqual(accounts[0].type, self._account_b.type)

    def test_get_list(self):
        self._account_repository.create(self._account_a)
        self._account_repository.create(self._account_b)

        account_list = self._account_repository.get_list()

        self.assertEqual(account_list[1], self._account_a.name)
        self.assertEqual(account_list[0], self._account_b.name)

    def test_get_id_by_name(self):
        self._account_repository.create(self._account_b)

        account_id = self._account_repository.get_id_by_name(self._account_b.name)

        self.assertEqual(account_id, 1)
