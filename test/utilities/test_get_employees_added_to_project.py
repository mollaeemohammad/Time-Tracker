from unittest import TestCase
from utilities.get_employee import get_employee
from utilities.add_new_project import add_new_project
from utilities.new_user import add_new_employee
from utilities.delete_employee import delete_employee
from utilities.add_employee_to_project import add_employee_to_project
from utilities.delete_project import delete_project


class TestGetEmployeesAddedToProject(TestCase):
    def test_get_all_employees(self):
        """Properly getting all employees that were added to the project"""
        add_new_project('test', 'test')
        add_new_employee('test', 'test', 'test', 'test')
        add_new_employee('test2', 'test2', 'test2', 'test2')
        self.assertNotEqual(add_employee_to_project('test', 'test'), -1)
        self.assertNotEqual(add_employee_to_project('test2', 'test'), -1)
        delete_project('test')
        delete_employee('test')
        delete_employee('test2')

