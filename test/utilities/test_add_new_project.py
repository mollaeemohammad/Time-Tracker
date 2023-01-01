from unittest import TestCase
from utilities.add_new_project import add_new_project
from utilities.delete_project import delete_project


class TestAddNewProject(TestCase):
    def test_insert(self):
        """Insert a project without any error or problem"""

        # delete the first project if already exists in database
        delete_project("first project")
        result = add_new_project(name="first project", description="A description")
        self.assertNotEqual(result, -1)
        delete_project("first project")
