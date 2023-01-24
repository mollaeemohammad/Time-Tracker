from unittest import TestCase
from flask_jwt_extended import create_access_token
from app import create_app
from utilities.delete_project import delete_project
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.delete_employee import delete_employee
from utilities.delete_employer import delete_employer
from utilities.new_user import add_new_employer, add_new_employee
from utilities.add_employee_to_project import add_employee_to_project
from utilities.insert_hours import insert_hours


class TestGetHoursOfAllEmployees(TestCase):
    def test_get(self):
        """Get hours of all employees without any error or problem by API"""
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employer('test', 'test', 'test', 'employer')
            add_new_employee('test', 'test', 'test', 'employee')
            add_new_employee('test', 'test', 'test', 'employee2')
            add_new_project_by_employer('employer', 'test', 'test')
            add_employee_to_project('employee', 'test')
            add_employee_to_project('employee2', 'test')
            insert_hours('employee', 'test', 1.6)
            insert_hours('employee2', 'test', 1.5)
            access_token = create_access_token('employer')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.get('http://127.0.0.1:5000/api/get_hours_of_all_employees',
                                json={'project_name': 'test'},
                                headers=headers)

            self.assertEqual(result.status_code, 200)
            self.assertIsNotNone(result.json)
            self.assertEqual(len(result.json), 2)
            delete_employer("employer")
            delete_employee('employee')
            delete_employee('employee2')
            delete_project('test')
