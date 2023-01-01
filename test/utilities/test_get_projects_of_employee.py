from unittest import TestCase
from utilities.add_employee_to_project import add_employee_to_project
from utilities.get_employee import get_employee
from utilities.add_new_project import add_new_project
from utilities.get_project import get_project
from utilities.new_user import add_new_employee
from utilities.get_projects_of_employee import get_projects_of_employee
from utilities.delete_project import delete_project
from utilities.delete_employee import delete_employee


class TestGetProjectsOfEmployee(TestCase):
    def test_get_good_case(self):
        """Get all projects of an employee"""
        add_new_project("test", "test")
        add_new_project("test2", "test2")
        add_new_employee('test', 'test', 'test', 'test')
        add_employee_to_project('test', 'test')
        add_employee_to_project('test', 'test2')
        self.assertEqual(len(get_projects_of_employee('test')), 2)
        delete_employee('test')
        delete_project('test')
        delete_project('test2')

    def test_not_existing_get(self):
        """Cannot get projects of employee, because employee is not added to any project"""
        add_new_employee('test', 'test', 'test', 'test')
        self.assertEqual(len(get_projects_of_employee('test')), 0)
        delete_employee('test')