from unittest import TestCase
from utilities.add_new_project import add_new_project
from utilities.delete_project import delete_project
from utilities.new_user import add_new_employer
from app import create_app
from flask_jwt_extended import create_access_token


class TestAddNewProjectAPI(TestCase):
    def test_insert(self):
        """Insert a project without any error or problem by API"""
        app = create_app()
        with app.app_context():
            client = app.test_client()
            delete_project('test')
            add_new_employer('test', 'test', 'test', 'test')
            access_token = create_access_token('test')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.post('http://127.0.0.1:5000/api/add_new_project',
                                 json={"project_name": "test", "description": "test"},
                                 headers=headers)

            self.assertEqual(result.status_code, 200)
            delete_project("test")
