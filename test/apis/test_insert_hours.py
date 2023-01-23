from unittest import TestCase
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.delete_project import delete_project
from utilities.delete_employer import delete_employer
from utilities.delete_employee import delete_employee
from utilities.new_user import add_new_employer, add_new_employee
from app import create_app
from flask_jwt_extended import create_access_token


class TestInsertHours(TestCase):
    def test_insert(self):
        """Insert hours worked by an employee without any error or problem by API"""
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employer('test', 'test', 'test', 'employer')
            add_new_employee('test', 'test', 'test', 'employee')
            add_new_project_by_employer('employer', 'test', 'test')
            access_token = create_access_token('employer')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.post('http://127.0.0.1:5000/api/insert_hours',
                                 json={"employee_username": "employee", "project_name": "test", "measured_hours": 10.0},
                                 headers=headers)

            self.assertEqual(result.status_code, 200)

            delete_project('test')
            delete_employer('employer')
            delete_employee('employee')
