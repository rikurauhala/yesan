import unittest

from file_handler import file_handler

from services.account_service import AccountService
from services.transaction_service import TransactionService

from repositories.transaction_repository import transaction_repository


class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self._file_handler = file_handler

        self._account_service = AccountService()
        self._account_service.delete_all()

        self._account_a_name = "Name A"
        self._account_a_type = "Type A"
        self._account_service.create_account(
            self._account_a_name, self._account_a_type)
        self._account_a_uuid = self._account_service.find_all()[0].id

        self._account_b_name = "Name B"
        self._account_b_type = "Type B"
        self._account_service.create_account(
            self._account_b_name, self._account_b_type)
        self._account_b_uuid = self._account_service.find_all()[1].id

        self._transaction_service = TransactionService()
        self._transaction_service.delete_all()

        self._transaction_a_date = "2022-01-01"
        self._transaction_a_amount = "1000"
        self._transaction_a_category = "Category A"
        self._transaction_a_description = "Description A"
        self._transaction_a_account_id = self._account_a_uuid
        self._transaction_a_party = "Receiver A"

        self._transaction_b_date = "2022-01-01"
        self._transaction_b_amount = "1000"
        self._transaction_b_category = "Category B"
        self._transaction_b_description = "Description B"
        self._transaction_b_account_id = self._account_b_uuid
        self._transaction_b_party = "Receiver B"

        self._transaction_repository = transaction_repository

    def test_convert_to_int(self):
        input_a = "10.00"
        result_a = self._transaction_service._convert_to_int(input_a)
        self.assertEqual(result_a, 1000)

        input_b = "10"
        result_b = self._transaction_service._convert_to_int(input_b)
        self.assertEqual(result_b, 1000)

        input_c = "10.01"
        result_c = self._transaction_service._convert_to_int(input_c)
        self.assertEqual(result_c, 1001)

        input_d = "10.1"
        result_d = self._transaction_service._convert_to_int(input_d)
        self.assertEqual(result_d, 1010)

    def test_create_transaction(self):
        success = self._transaction_service.create_transaction(
            self._transaction_a_date,
            self._transaction_a_amount,
            self._transaction_a_category,
            self._transaction_a_description,
            self._transaction_a_account_id,
            self._transaction_a_party
        )
        transactions = self._transaction_service.find_all()
        self.assertTrue(success)
        self.assertEqual(len(transactions), 1)

    def test_format_amount(self):
        input_a = None
        result_a = self._transaction_service.format_amount(input_a)
        self.assertEqual(result_a, "0,00 €")

        input_b = 10000
        result_b = self._transaction_service.format_amount(input_b)
        self.assertEqual(result_b, "100,00 €")

        input_c = 123456789
        result_c = self._transaction_service.format_amount(input_c)
        self.assertEqual(result_c, "1 234 567,89 €")

        input_d = "String"
        result_d = self._transaction_service.format_amount(input_d)
        self.assertEqual(result_d, "0,00 €")

    def test_find_all_as_list(self):
        success = self._transaction_service.create_transaction(
            self._transaction_a_date,
            self._transaction_a_amount,
            self._transaction_a_category,
            self._transaction_a_description,
            self._transaction_a_account_id,
            self._transaction_a_party
        )
        self.assertTrue(success)
        success = self._transaction_service.create_transaction(
            self._transaction_b_date,
            self._transaction_b_amount,
            self._transaction_b_category,
            self._transaction_b_description,
            self._transaction_b_account_id,
            self._transaction_b_party
        )
        self.assertTrue(success)
        transactions = self._transaction_service.find_all_as_list()
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0][0], self._transaction_a_date)
        amount = self._transaction_service.format_amount(
            int(self._transaction_a_amount)*100)
        self.assertEqual(transactions[0][1], amount)
        self.assertEqual(transactions[0][2], self._transaction_a_category)
        self.assertEqual(transactions[0][3], self._transaction_a_description)
        self.assertEqual(transactions[0][4], self._account_a_name)
        self.assertEqual(transactions[0][5], self._transaction_a_party)

    def test_find_all_with_id(self):
        success = self._transaction_service.create_transaction(
            self._transaction_b_date,
            self._transaction_b_amount,
            self._transaction_b_category,
            self._transaction_b_description,
            self._transaction_b_account_id,
            self._transaction_b_party
        )
        self.assertTrue(success)
        transactions = self._transaction_service.find_all_with_id()
        self.assertEqual(len(transactions), 1)

    def test_get_balance_by_id(self):
        success = self._transaction_service.create_transaction(
            self._transaction_a_date,
            self._transaction_a_amount,
            self._transaction_a_category,
            self._transaction_a_description,
            self._transaction_a_account_id,
            self._transaction_a_party
        )
        self.assertTrue(success)
        success = self._transaction_service.create_transaction(
            self._transaction_b_date,
            self._transaction_b_amount,
            self._transaction_b_category,
            self._transaction_b_description,
            self._transaction_b_account_id,
            self._transaction_b_party
        )
        self.assertTrue(success)
        balance = self._transaction_service.get_balance_by_id(
            self._account_a_uuid)
        self.assertEqual(balance, 100000)

    def test_calculate_net_worth(self):
        success = self._transaction_service.create_transaction(
            self._transaction_a_date,
            self._transaction_a_amount,
            self._transaction_a_category,
            self._transaction_a_description,
            self._transaction_a_account_id,
            self._transaction_a_party
        )
        self.assertTrue(success)
        net_worth = self._transaction_service.calculate_net_worth()
        self.assertEqual(net_worth, 100000)

    def test_import_transactions(self):
        success = self._transaction_service.create_transaction(
            self._transaction_a_date,
            self._transaction_a_amount,
            self._transaction_a_category,
            self._transaction_a_description,
            self._transaction_a_account_id,
            self._transaction_a_party
        )
        self.assertTrue(success)
        success = self._transaction_service.export_transactions()
        self.assertTrue(success)
        transactions = self._file_handler.import_transactions()
        self.assertEqual(len(transactions), 1)

    def test_export_transactions(self):
        success = self._transaction_service.create_transaction(
            self._transaction_a_date,
            self._transaction_a_amount,
            self._transaction_a_category,
            self._transaction_a_description,
            self._transaction_a_account_id,
            self._transaction_a_party
        )
        self.assertTrue(success)
        success = self._transaction_service.export_transactions()
        self.assertTrue(success)
