from unittest import TestCase
from flask_jwt_extended import create_access_token
from app import create_app
from utilities.add_employee_to_project import add_employee_to_project
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.delete_employee import delete_employee
from utilities.delete_employer import delete_employer
from utilities.delete_project import delete_project
from utilities.new_user import add_new_employer, add_new_employee


class TestUpdateFee(TestCase):
    def test_delete(self):
        """Update fee of a project for an employee without any error or problem by API"""
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employer('test', 'test', 'test', 'employer')
            add_new_employee('test', 'test', 'test', 'employee')
            add_new_project_by_employer('employer', 'test', 'test')
            add_employee_to_project('employee', 'test')
            access_token = create_access_token('employer')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            # project_name: str, employee_username: str, new_fee: float
            result = client.post('http://127.0.0.1:5000/api/update_fee',
                                 json={"project_name": "test", "employee_username": "employee", 'new_fee': 2.0},
                                 headers=headers)

            self.assertEqual(result.status_code, 200)
            self.assertEqual(result.json['message'], 'Successful')
            delete_employer('employer')
            delete_employee('employee')
            delete_project("test")
