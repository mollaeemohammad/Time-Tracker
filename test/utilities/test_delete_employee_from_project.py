from unittest import TestCase
from utilities.delete_employee_from_project import delete_employee_from_project
from utilities.add_employee_to_project import add_employee_to_project
from utilities.get_employee import get_employee
from utilities.get_project import get_project
from utilities.new_user import add_new_employee
from utilities.add_new_project import add_new_project
from utilities.delete_employee import delete_employee
from utilities.delete_project import delete_project


class TestDeleteEmployeeFromProject(TestCase):
    def test_delete_good_case(self):
        """Delete employee from a project"""
        add_new_project('test', 'test')
        add_new_employee('test', 'test', 'test', 'test')
        add_employee_to_project(employee_username='test', project_name='test')
        self.assertEqual(delete_employee_from_project('test', 'test'), 1)
        delete_project('test')
        delete_employee('test')
