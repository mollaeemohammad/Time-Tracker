#
#
#
#
# from unittest import TestCase
# # from utilities.delete_employee import delete_employee
# from utilities.new_user import add_new_employee
# from utilities.delete_employee import delete_employee
# from app import create_app
#
#
# class TestDeleteEmployee(TestCase):
#     def test_delete_good_case(self):
#         """Properly delete the already existing employee"""
#         client = create_app().test_client()
#         delete_employee('test')
#         add_new_employee('test', 'test', 'test', 'test')
#         client.post()
#         delete_employee('test')
#
#
#
#
#
#
# with app.test_client() as c:
#     rv = c.get('/users', json={})
#     print(rv.data)
#     print('status: ', rv.status_code)