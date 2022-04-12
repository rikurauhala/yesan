import unittest

from entities.account import Account

from database.database_operations import database_connection

from repositories.account_repository import AccountRepository


class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        self._account_repository = AccountRepository(database_connection)
        self._account_repository.delete_all()

        name_checking_account = "Checking account"
        type_checking_account = "Bank account"
        self.account_checking_account = Account(None, name_checking_account, type_checking_account)

        name_bitcoin = "Bitcoin"
        type_bitcoin= "Crypto currency"
        self.account_bitcoin = Account(None, name_bitcoin, type_bitcoin)

    def test_create(self):
        self._account_repository.create(self.account_bitcoin)
        accounts = self._account_repository.find_all()

        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].id, 1)
        self.assertEqual(accounts[0].name, self.account_bitcoin.name)
        self.assertEqual(accounts[0].type, self.account_bitcoin.type)
