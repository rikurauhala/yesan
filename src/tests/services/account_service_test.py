from cgi import test
import unittest

from services.account_service import AccountService


class TestAccountService(unittest.TestCase):
    def setUp(self):
        self._account_service = AccountService()
        self._account_service.delete_all()

        self._name_account_a = "Checking account"
        self._type_account_a = "Bank account"

        self._name_account_b = "Bitcoin"
        self._type_account_b = "Crypto currency"

    def test_create_account(self):
        self._account_service.create_account(
            self._name_account_b,
            self._type_account_b
        )
        accounts = self._account_service.find_all()

        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].name, self._name_account_b)
        self.assertEqual(accounts[0].type, self._type_account_b)

    def test_get_list(self):
        self._account_service.create_account(
            self._name_account_a,
            self._type_account_a
        )
        self._account_service.create_account(
            self._name_account_b,
            self._type_account_b
        )

        account_list = self._account_service.get_list()

        self.assertEqual(account_list[1], self._name_account_a)
        self.assertEqual(account_list[0], self._name_account_b)

    def test_get_id_by_name(self):
        self._account_service.create_account(
            self._name_account_b,
            self._type_account_b
        )
        accounts = self._account_service.find_all()
        id_expected = accounts[0].id
        id_actual = self._account_service.get_id_by_name(self._name_account_b)

        self.assertEqual(len(accounts), 1)
        self.assertEqual(id_actual, id_expected)
