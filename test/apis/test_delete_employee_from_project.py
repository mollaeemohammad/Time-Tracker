from unittest import TestCase
from utilities.add_new_project import add_new_project
from utilities.delete_project import delete_project
from utilities.new_user import add_new_employee
from utilities.get_employee import get_employee
from utilities.delete_employee import delete_employee
from utilities.add_employee_to_project import add_employee_to_project
from utilities.get_employees_added_to_project import get_employees_added_to_project
from app import create_app
from flask_jwt_extended import create_access_token


class TestDeleteEmployeeFromProject(TestCase):
    def test_delete(self):
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employee('test', 'test', 'test', 'test')
            add_new_project('test', 'test')
            add_employee_to_project('test', 'test')
            access_token = create_access_token('test')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.post('http://127.0.0.1:5000/api/delete_employee_from_project',
                                 json={"employee_username": 'test', "project_name": 'test'},
                                 headers=headers)

            self.assertEqual(result.status_code, 200)
            self.assertEqual(len(get_employees_added_to_project('test')), 0)
            delete_project("test")
            delete_employee('test')
