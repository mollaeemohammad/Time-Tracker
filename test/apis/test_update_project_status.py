from unittest import TestCase
from flask_jwt_extended import create_access_token
from app import create_app
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.delete_employer import delete_employer
from utilities.delete_project import delete_project
from utilities.get_project import get_project
from utilities.new_user import add_new_employer


class TestUpdateProjectStatus(TestCase):
    def test_delete(self):
        """Update status of a project without any error or problem by API"""
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employer('test', 'test', 'test', 'test')
            add_new_project_by_employer('test', 'test', 'test')
            access_token = create_access_token('test')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.post('http://127.0.0.1:5000/api/update_project_status',
                                 json={"project_name": "test", "new_status": "new test"},
                                 headers=headers)

            self.assertEqual(result.status_code, 200)
            self.assertEqual(get_project('test')[5], 'new test')
            delete_employer('test')
            delete_project("test")
