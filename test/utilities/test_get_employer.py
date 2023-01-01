from unittest import TestCase
from utilities.get_employer import get_employer
from utilities.new_user import add_new_employer
from utilities.delete_employer import delete_employer


class TestGetEmployer(TestCase):
    def test_get_good_case(self):
        """Get an already existing employer"""
        delete_employer('test')
        add_new_employer('test', 'test', 'test', 'test')
        self.assertIsNotNone(get_employer('test'))
        delete_employer('test')

    def test_get_not_existing_case(self):
        """Cannot find a not existing employer"""
        delete_employer('testasdfghffkrtui')
        self.assertIsNone(get_employer('testasdfghffkrtui'))
