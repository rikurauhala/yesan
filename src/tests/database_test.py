import uuid

import unittest

from database_operations import database_connection


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self._test_uuid = str(uuid.uuid4())
        self._test_name = "Name"
        self._test_type = "Type"

    def test_accounts_table(self):
        cursor = database_connection.cursor()
        cursor.execute("""
            INSERT INTO accounts (id, name, type)
            VALUES (?, ?, ?)
        """, (self._test_uuid, self._test_name, self._test_type))
        database_connection.commit()

        cursor.execute("""
            SELECT * FROM accounts WHERE name=(?);
        """, (self._test_name, ))

        values = cursor.fetchone()
        id = values[0]
        name = values[1]
        type = values[2]

        self.assertEqual(id, self._test_uuid)
        self.assertEqual(name, self._test_name)
        self.assertEqual(type, self._test_type)
