import unittest

from database_operations import database_connection


class TestDatabase(unittest.TestCase):
    def setUp(self):
        pass

    def test_accounts_table(self):
        cursor = database_connection.cursor()
        cursor.execute("""
            INSERT INTO accounts (id, name, type)
            VALUES (0, 'test-name', 'test-type')
        """)
        database_connection.commit()

        cursor.execute("""
            SELECT * FROM accounts WHERE name='test-name';
        """)

        values = cursor.fetchone()
        id = values[0]
        name = values[1]
        type = values[2]

        self.assertEqual(id, 0)
        self.assertEqual(name, "test-name")
        self.assertEqual(type, "test-type")
