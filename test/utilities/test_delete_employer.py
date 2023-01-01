from unittest import TestCase
from utilities.delete_employer import delete_employer
from utilities.new_user import add_new_employer


class TestDeleteEmployer(TestCase):
    def test_delete_good_case(self):
        """Properly delete the already existing employee"""
        delete_employer('test')
        add_new_employer('test', 'test', 'test', 'test')
        self.assertEqual(delete_employer('test'), 1)

    def test_delete_not_existing_case(self):
        """Cannot delete a not existing employer"""
        self.assertEqual(delete_employer('asdfqwetrggsadfgdfh'), 0)
