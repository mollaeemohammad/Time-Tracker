from unittest import TestCase
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.delete_project import delete_project
from utilities.new_user import add_new_employer
from utilities.delete_employer import delete_employer


class TestAddNewProjectByEmployer(TestCase):
    def test_insert(self):
        """Add new project by a fake employer"""
        delete_project("test")
        add_new_employer('test', 'test', 'test', 'test')
        result = add_new_project_by_employer(name="test",
                                             description="test",
                                             employer_username='test')
        self.assertNotEqual(result, -1)
        delete_project("test")
        delete_employer('test')
