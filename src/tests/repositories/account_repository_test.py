import unittest

import uuid

from database import database_connection as connection

from entities.account import Account

from repositories.account_repository import AccountRepository


class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        self._account_repository = AccountRepository(connection)
        self._account_repository.delete_all()

        self._uuid_account_a = str(uuid.uuid4())
        self._name_account_a = "Name A"
        self._type_account_a = "Type A"
        self._account_a = Account(
            self._uuid_account_a,
            self._name_account_a,
            self._type_account_a
        )

        self._uuid_account_b = str(uuid.uuid4())
        self._name_account_b = "Name B"
        self._type_account_b = "Type B"
        self._account_b = Account(
            self._uuid_account_b,
            self._name_account_b,
            self._type_account_b
        )

    def test_create(self):
        self._account_repository.create(
            self._account_a,
        )
        accounts = self._account_repository.find_all()

        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].name, self._name_account_a)
        self.assertEqual(accounts[0].type, self._type_account_a)

    def test_get_list(self):
        self._account_repository.create(self._account_a)
        self._account_repository.create(self._account_b)

        account_list = self._account_repository.get_list()

        self.assertEqual(account_list[0], self._name_account_a)
        self.assertEqual(account_list[1], self._name_account_b)

    def test_get_id_by_name(self):
        pass
