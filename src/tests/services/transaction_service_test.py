import unittest

from services.transaction_service import TransactionService


class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self._transaction_service = TransactionService()
        self._transaction_service.delete_all()

        self._date_transaction_a = "2022-01-01"
        self._amount_transaction_a = "-9999"
        self._category_transaction_a = "Category A"
        self._description_transaction_a = "Description A"
        self._account_id_transaction_a = "Account_id A"
        self._party_transaction_a = "Receiver A"

    def test_create_transaction(self):
        self._transaction_service.create_transaction(
            self._date_transaction_a,
            self._amount_transaction_a,
            self._category_transaction_a,
            self._description_transaction_a,
            self._account_id_transaction_a,
            self._party_transaction_a
        )
        transactions = self._transaction_service.find_all()
