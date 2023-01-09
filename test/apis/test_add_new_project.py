# from unittest import TestCase
# from utilities.add_new_project import add_new_project
# from utilities.delete_project import delete_project
# from app import create_app
# from flask_jwt_extended import create_access_token
#
#
# class TestAddNewProjectAPI(TestCase):
#     def test_insert(self):
#         """Insert a project without any error or problem by API"""
#         app = create_app()
#         with app.app_context():
#             client = app.test_client()
#             delete_project("first project")
#             access_token = create_access_token('sdf')
#             headers = {
#                 'Authorization': 'Bearer {}'.format(access_token)
#             }
#             result = client.post('/api/add_new_project',
#                                  json={"name": "first project", "description": "A description"},
#                                  headers=headers)
#             print('here is what just happend\n\n')
#             print(result)
#             print('\n\nhere is what just happend')
#             self.assertNotEqual(result, -1)
#             delete_project("first project")
