import unittest

from services.account_service import AccountService
from services.transaction_service import TransactionService


class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self._account_service = AccountService()
        self._account_service.delete_all()

        self._account_a_name = "Name A"
        self._account_a_type = "Type A"

        self._account_service.create_account(
            self._account_a_name,
            self._account_a_type
        )

        self._account_a_uuid = self._account_service.find_all()[0].id

        self._transaction_service = TransactionService()
        self._transaction_service.delete_all()

        self._transaction_a_date = "2022-01-01"
        self._transaction_a_amount = "-9999"
        self._transaction_a_category = "Category A"
        self._transaction_a_description = "Description A"
        self._transaction_a_account_id = self._account_a_uuid
        self._transaction_a_party = "Receiver A"

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
