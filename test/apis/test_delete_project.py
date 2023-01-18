from unittest import TestCase
from utilities.delete_project import delete_project
from utilities.new_user import add_new_employer
from utilities.get_project import get_project
from utilities.add_new_project import add_new_project
from utilities.add_employee_to_project import add_employee_to_project
from app import create_app
from flask_jwt_extended import create_access_token


class TestDeleteProject(TestCase):
    def test_delete(self):
        """Insert a project without any error or problem by API"""
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employer('test', 'test', 'test', 'test')
            add_new_project('test', 'test')
            add_employee_to_project('test', 'test')

            access_token = create_access_token('test')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.post('http://127.0.0.1:5000/api/delete_project',
                                 json={"project_name": "test"},
                                 headers=headers)

            self.assertEqual(result.status_code, 200)
            self.assertIsNone(get_project('test'))
            delete_project("test")
