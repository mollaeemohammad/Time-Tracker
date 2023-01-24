from unittest import TestCase
from flask_jwt_extended import create_access_token
from app import create_app
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.delete_employee import delete_employee
from utilities.delete_employer import delete_employer
from utilities.delete_project import delete_project
from utilities.new_user import add_new_employer, add_new_employee
from utilities.insert_hours import insert_hours


class TestGetHoursOfEmployee(TestCase):
    def test_get(self):
        """Get summation of hours of an employee without any error or problem by API"""
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employer('test', 'test', 'test', 'employer')
            add_new_employee('test', 'test', 'test', 'employee')
            add_new_project_by_employer('employer', 'test', 'test')
            insert_hours('employee', 'test', 1.5)
            insert_hours('employee', 'test', 1.5)
            access_token = create_access_token('employer')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.get('http://127.0.0.1:5000/api/get_total_hours_of_employee',
                                json={"employee_username": "employee", 'project_name': 'test'},
                                headers=headers)

            self.assertEqual(result.status_code, 200)
            self.assertIsNotNone(result.json)
            self.assertEqual(result.json['total_hours'], 3.0)
            delete_employer("employer")
            delete_employee('employee')
            delete_project('test')
