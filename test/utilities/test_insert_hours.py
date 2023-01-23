from unittest import TestCase
from utilities.add_new_project import add_new_project
from utilities.delete_project import delete_project
from utilities.delete_employer import delete_employer
from utilities.delete_employee import delete_employee
from utilities.insert_hours import insert_hours
from utilities.new_user import add_new_employer, add_new_employee
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.add_employee_to_project import add_employee_to_project



class TestInsertHours(TestCase):
    def test_insert(self):
        """Insert a project without any error or problem"""

        # delete the first project if already exists in database
        delete_project("test")
        add_new_employer('test', 'test', 'test', 'test')
        add_new_employee('test', 'test', 'test', 'test')
        add_new_project_by_employer('test', 'test', 'test')
        add_employee_to_project('test', 'test')
        result = insert_hours('test', 'test', 1.6)
        self.assertNotEqual(result, -1)
        delete_project("test")
        delete_employer('test')
        delete_employee('test')

