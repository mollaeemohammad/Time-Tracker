from unittest import TestCase
from flask_jwt_extended import create_access_token
from app import create_app
from utilities.delete_employee import delete_employee
from utilities.new_user import add_new_employee


class TestGetEmployee(TestCase):
    def test_get(self):
        """Get a project without any error or problem by API"""
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employee('test', 'test', 'test', 'test')
            access_token = create_access_token('test')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.get('http://127.0.0.1:5000/api/get_employee',
                                 json={"username": "test"},
                                 headers=headers)

            self.assertEqual(result.status_code, 200)
            self.assertIsNotNone(result.json)
            delete_employee("test")
