from unittest import TestCase
from utilities.add_new_project import add_new_project
from utilities.add_employee_to_project import add_employee_to_project
from utilities.delete_employee import delete_employee
from utilities.delete_project import delete_project
from utilities.get_hours_of_employee import get_hours_of_employee
from utilities.insert_hours import insert_hours
from utilities.new_user import add_new_employee


class TestGetHoursOfEmployee(TestCase):
    def test_get_all_hours(self):
        """Properly getting all hours that one employee worked on the project"""
        add_new_project('test', 'test')
        add_new_employee('test', 'test', 'test', 'employee')
        add_employee_to_project('employee', 'test')
        insert_hours('employee', 'test', 10.0)
        insert_hours('employee', 'test', 10.0)
        self.assertEqual(len(get_hours_of_employee("employee", 'test')), 2)
        delete_project('test')
        delete_employee('employee')
