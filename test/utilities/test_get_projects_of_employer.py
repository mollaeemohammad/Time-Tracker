from unittest import TestCase
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.get_employee import get_employee
from utilities.get_project import get_project
from utilities.new_user import add_new_employer
from utilities.get_projects_of_employer import get_projects_of_employer
from utilities.delete_project import delete_project
from utilities.delete_employer import delete_employer


class TestGetProjectsOfEmployee(TestCase):
    def test_get_good_case(self):
        """Get all projects of an employee"""
        add_new_employer('test', 'test', 'test', 'test')
        add_new_project_by_employer(employer_username='test',
                                    name='test',
                                    description='test')
        add_new_project_by_employer(employer_username='test',
                                    name='test2',
                                    description='test2')
        self.assertEqual(len(get_projects_of_employer('test')), 2)
        delete_employer('test')
        delete_project('test')
        delete_project('test2')

    def test_not_existing_get(self):
        """Cannot get projects of employee, because employee is not added to any project"""
        delete_employer('test')
        add_new_employer('test', 'test', 'test', 'test')
        self.assertEqual(len(get_projects_of_employer('test')), 0)
        delete_employer('test')
