from unittest import TestCase
from flask_jwt_extended import create_access_token
from app import create_app
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.delete_employee import delete_employee
from utilities.delete_employer import delete_employer
from utilities.delete_project import delete_project
from utilities.new_user import add_new_employer, add_new_employee


class TestGetProjectsOfEmployee(TestCase):
    def test_get(self):
        """Get projects of an employee without any error or problem by API"""
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employer('test', 'test', 'test', 'employer')
            add_new_employee('test', 'test', 'test', 'employee')
            add_new_project_by_employer('employer', 'test', 'test')
            add_new_project_by_employer('employer', 'test2', 'test2')

            access_token = create_access_token('employee')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.get('http://127.0.0.1:5000/api/get_projects_of_employee',
                                headers=headers)

            self.assertEqual(result.status_code, 200)
            self.assertIsNotNone(result.json)
            delete_employer('employer')
            delete_employee('employee')
            delete_project('test')
            delete_project('test2')
