from unittest import TestCase
from utilities.delete_employee import delete_employee
from utilities.new_user import add_new_employee


class TestDeleteEmployee(TestCase):
    def test_delete_good_case(self):
        """Properly delete the already existing employee"""
        delete_employee('test')
        self.assertNotEqual(add_new_employee('test', 'test', 'test', 'test'), -1)
        delete_employee('test')
