from unittest import TestCase
from utilities.delete_project import delete_project
from utilities.new_user import add_new_employee
from utilities.delete_employee import delete_employee
from utilities.add_employee_to_project import add_employee_to_project
from utilities.get_employees_added_to_project import get_employees_added_to_project
from utilities.add_new_project_by_employer import add_new_project_by_employer
from app import create_app
from flask_jwt_extended import create_access_token


class TestGetEmployeesAddedToProject(TestCase):
    def test_get(self):
        app = create_app()
        with app.app_context():
            client = app.test_client()
            add_new_employee('test', 'test', 'test', 'test')
            add_new_employee('test2', 'test2', 'test2', 'test2')
            add_new_project_by_employer('test', 'test', 'test')
            add_employee_to_project('test', 'test')
            add_employee_to_project('test2', 'test')
            access_token = create_access_token('test')
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            result = client.get('http://127.0.0.1:5000/api/get_employees_added_to_project',
                                json={"project_name": 'test'},
                                headers=headers)

            self.assertEqual(result.status_code, 200)
            self.assertEqual(len(result.json), 2)
            delete_project("test")
            delete_employee('test')
            delete_employee('test2')
