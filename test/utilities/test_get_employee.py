from unittest import TestCase
from utilities.get_employee import get_employee
from utilities.new_user import add_new_employee
from utilities.delete_employee import delete_employee


class TestGetEmployee(TestCase):
    def test_get_good_case(self):
        """Get an already existing employee"""
        delete_employee('test')
        add_new_employee('test', 'test', 'test', 'test')
        self.assertIsNotNone(get_employee('test'))
        delete_employee('test')

    def test_get_not_existing_case(self):
        """Cannot find a not existing employee"""
        delete_employee('testwerppjjpj')
        self.assertIsNone(get_employee('testwerppjjpj'))
