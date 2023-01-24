from unittest import TestCase
from utilities.delete_project import delete_project
from utilities.add_new_project import add_new_project


class TestDeleteProject(TestCase):
    def test_delete_project(self):
        """Delete project from database and check deletion of dependencies"""
        add_new_project("test add new project", "asdf")
        self.assertEqual(delete_project("test add new project"), 1)

    def test_delete_not_existing_project(self):
        """Cannot delete not existing project"""
        self.assertEqual(delete_project("not existing project"), 0)
