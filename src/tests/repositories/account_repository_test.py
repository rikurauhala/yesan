import unittest

import uuid

from database import database_connection as connection

from entities.account import Account

from repositories.account_repository import AccountRepository


class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        self._account_repository = AccountRepository(connection)
        self._account_repository.delete_all()

        self._account_a = Account(
            account_id=str(uuid.uuid4()),
            account_name="Name A",
            account_type="Type A"
        )

        self._account_b = Account(
            account_id=str(uuid.uuid4()),
            account_name="Name B",
            account_type="Type B"
        )

    def test_create(self):
        success = self._account_repository.create(self._account_a)
        self.assertTrue(success)

        accounts = self._account_repository.find_all()
        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].name, self._account_a.name)
        self.assertEqual(accounts[0].type, self._account_a.type)

    def test_create_integrity_error(self):
        success = self._account_repository.create(self._account_a)
        self.assertTrue(success)

        accounts = self._account_repository.find_all()
        self.assertEqual(len(accounts), 1)

        success = self._account_repository.create(self._account_a)
        self.assertFalse(success)

        accounts = self._account_repository.find_all()
        self.assertEqual(len(accounts), 1)

    def test_get_list(self):
        self._account_repository.create(self._account_a)
        self._account_repository.create(self._account_b)

        account_list = self._account_repository.get_list()

        self.assertEqual(account_list[0], self._account_a.name)
        self.assertEqual(account_list[1], self._account_b.name)

    def test_get_id_by_name(self):
        pass
