from unittest import TestCase
from utilities.add_new_project import add_new_project
from utilities.delete_project import delete_project
from utilities.new_user import add_new_employee
from utilities.get_employee import get_employee
from app import create_app
from flask_jwt_extended import create_access_token


class TestDeleteEmployee(TestCase):
    def test_delete(self):
        """Insert a project without any error or problem by API"""
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employee('test', 'test', 'test', 'test')
            access_token = create_access_token('test')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.post('http://127.0.0.1:5000/api/delete_employee',
                                 headers=headers)

            self.assertIsNone(get_employee('test'))
            delete_project("test")
