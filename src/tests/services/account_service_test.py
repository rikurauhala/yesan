import unittest

from file_handler import file_handler

from services.account_service import AccountService


class TestAccountService(unittest.TestCase):
    def setUp(self):
        self._account_service = AccountService()
        self._account_service.delete_all()

        self._account_a_name = "Name A"
        self._account_a_type = "Type A"

        self._account_b_name = "Name B"
        self._account_b_type = "Type"

        self._file_handler = file_handler

    def test_create_account(self):
        self._account_service.create_account(
            self._account_b_name,
            self._account_b_type
        )
        accounts = self._account_service.find_all()

        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].name, self._account_b_name)
        self.assertEqual(accounts[0].type, self._account_b_type)

    def test_get_list(self):
        self._account_service.create_account(
            self._account_a_name,
            self._account_a_type
        )
        self._account_service.create_account(
            self._account_b_name,
            self._account_b_type
        )

        account_list = self._account_service.get_list()

        self.assertEqual(account_list[0], self._account_a_name)
        self.assertEqual(account_list[1], self._account_b_name)

    def test_get_id_by_name(self):
        self._account_service.create_account(
            self._account_b_name,
            self._account_b_type
        )
        accounts = self._account_service.find_all()
        id_expected = accounts[0].id
        id_actual = self._account_service.get_id_by_name(self._account_b_name)

        self.assertEqual(len(accounts), 1)
        self.assertEqual(id_actual, id_expected)

    def test_import_accounts(self):
        success = self._account_service.create_account(
            self._account_b_name,
            self._account_b_type
        )
        self.assertTrue(success)
        success = self._account_service.export_accounts()
        self.assertTrue(success)
        accounts = self._file_handler.import_accounts()
        self.assertEqual(len(accounts), 1)

    def test_export_accounts(self):
        success = self._account_service.create_account(
            self._account_b_name,
            self._account_b_type
        )
        self.assertTrue(success)
        success = self._account_service.export_accounts()
        self.assertTrue(success)
