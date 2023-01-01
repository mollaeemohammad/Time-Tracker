from unittest import TestCase
from utilities.get_project import get_project
from utilities.add_new_project import add_new_project
from utilities.delete_project import delete_project


class TestGetProject(TestCase):
    def test_get_project_good_case(self):
        """Find and return an already existing project"""
        delete_project('first project')
        add_new_project('first project', "just for test")
        self.assertIn("first project", get_project("first project"))
        delete_project('first project')

    def test_fail_to_get_project(self):
        """Fail to find a fake project"""
        self.assertIsNone(get_project("asdfqwer"))
