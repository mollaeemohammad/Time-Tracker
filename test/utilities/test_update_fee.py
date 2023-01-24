from unittest import TestCase
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.delete_employer import delete_employer
from utilities.delete_employee import delete_employee
from utilities.delete_project import delete_project
from utilities.new_user import add_new_employer, add_new_employee
from utilities.update_fee import update_fee


class TestUpdateFee(TestCase):
    def test_update_good_case(self):
        """Update description successfully"""
        add_new_employer('test', 'test', 'test', 'employer')
        add_new_employee('test', 'test', 'test', 'employee')
        add_new_project_by_employer('employer', 'test', 'test')
        update_result = update_fee('test', 'employee', 2.0)
        self.assertNotEqual(update_result, -1)
        delete_project('test')
        delete_employer('employer')
        delete_employee('employee')
