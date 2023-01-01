from unittest import TestCase
from utilities.add_employee_to_project import add_employee_to_project
from utilities.get_employee import get_employee
from utilities.get_project import get_project
from utilities.new_user import add_new_employee
from utilities.add_new_project import add_new_project
from utilities.delete_employee_from_project import delete_employee_from_project
from utilities.delete_project import delete_project
from utilities.delete_employee import delete_employee


class TestAddEmployeeToProject(TestCase):
    def test_add_employee(self):
        """Employee is added then deleted from database"""
        add_new_project('test', 'test')
        add_new_employee('test', 'test', 'test', 'test')
        self.assertNotEqual(add_employee_to_project(employee_username='test', project_name='test'), -1)
        delete_project('test')
        delete_employee('test')
        delete_employee_from_project('test', 'test')
