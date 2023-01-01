from unittest import TestCase
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.get_employee import get_employee
from utilities.get_project import get_project
from utilities.new_user import add_new_employer
from utilities.get_projects_of_employer import get_projects_of_employer
from utilities.delete_project import delete_project
from utilities.delete_employer import delete_employer
from utilities.update_project_status import update_project_status


class TestUpdateProjectStatus(TestCase):
    def test_update_good_case(self):
        """Update status successfully"""
        add_new_employer('test', 'test', 'test', 'test')
        add_new_project_by_employer('test', 'test', 'test')
        update_result = update_project_status(project_name='test',
                                              new_status='new')
        project = get_project('test')
        project_new_description = project[5]

        self.assertNotEqual(update_result, -1)
        self.assertEqual(project_new_description, 'new')

        delete_project('test')
        delete_employer('test')
