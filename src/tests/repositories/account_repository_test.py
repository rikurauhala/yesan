import unittest

from entities.account import Account

from database_operations import database_connection as connection

from repositories.account_repository import AccountRepository


class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        self._account_repository = AccountRepository(connection)
        self._account_repository.delete_all()

        self._name_account_a = "Checking account"
        self._type_account_a = "Bank account"

        self._name_account_b = "Bitcoin"
        self._type_account_b = "Crypto currency"

    def test_create(self):
        self._account_repository.create(self._name_account_b, self._type_account_b)
        accounts = self._account_repository.find_all()

        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].name, self._name_account_b)
        self.assertEqual(accounts[0].type, self._type_account_b)

    def test_get_list(self):
        self._account_repository.create(self._name_account_a, self._type_account_a)
        self._account_repository.create(self._name_account_b, self._type_account_b)

        account_list = self._account_repository.get_list()

        self.assertEqual(account_list[1], self._name_account_a)
        self.assertEqual(account_list[0], self._name_account_b)

    def test_get_id_by_name(self):
        pass
