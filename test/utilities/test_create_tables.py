from unittest import TestCase
from utilities.create_tables import create_tables


class TestCreateTables(TestCase):
    def test_all_tables_are_up(self):
        """All tables are created properly"""
        self.assertEqual(create_tables(), 1)
