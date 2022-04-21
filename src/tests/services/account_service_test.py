import unittest

from entities.account import Account

from database_operations import database_connection as connection

from services.account_service import AccountService


class TestAccountService(unittest.TestCase):
    def setUp(self):
        self._account_service = AccountService()
        self._account_service.delete_all()

        name_account_a = "Checking account"
        type_account_a = "Bank account"
        self._account_a = Account(None, name_account_a, type_account_a)

        name_account_b = "Bitcoin"
        type_account_b = "Crypto currency"
        self._account_b = Account(None, name_account_b, type_account_b)

    def test_create_account(self):
        self._account_service.create_account(
            self._account_b.name, 
            self._account_b.type
        )
        accounts = self._account_service.find_all()

        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].id, 1)
        self.assertEqual(accounts[0].name, self._account_b.name)
        self.assertEqual(accounts[0].type, self._account_b.type)

    def test_get_list(self):
        self._account_service.create_account(
            self._account_a.name,
            self._account_a.type
        )
        self._account_service.create_account(
            self._account_b.name,
            self._account_b.type
        )

        account_list = self._account_service.get_list()

        self.assertEqual(account_list[1], self._account_a.name)
        self.assertEqual(account_list[0], self._account_b.name)

    def test_get_id_by_name(self):
        pass
