from flask import jsonify, g, current_app, session
from flask_restful import Resource, reqparse
from utilities.login import login_employee, login_employer
from utilities.errors import *
from utilities.new_user import add_new_employee, add_new_employer
from flask_jwt_extended import create_access_token


def is_found_user(mysql_response: list) -> bool:
    if len(mysql_response) != 0 and mysql_response != ['Something went wrong']:
        return True
    return False


class SignUpEmployee(Resource):
    def post(self):
        try:
            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('first_name', type=str, required=True)
            parser.add_argument('last_name', type=str, required=True)
            parser.add_argument('username', type=str, required=True)
            parser.add_argument('password', type=str, required=True)
            parser.add_argument('confirm_password', type=str, required=True)

            args = parser.parse_args()

            if args['password'] != args['confirm_password']:
                raise NotMatchPasswordWithConfirmError

            if ('logged_in' in list(session.keys())) and session['logged_in']:
                raise AlreadyIsLoggedInError

            login_employee_info = login_employee(args['username'], args['password'])

            if is_found_user(login_employee_info):
                raise AlreadyExistsError

            add_employee = add_new_employee(
                args['first_name'],
                args['last_name'],
                args['password'],
                args['username']
            )

            if add_employee == -1:
                raise AlreadyExistsError

            return jsonify({
                "message": "Successful",
            })

        except AlreadyExistsError:
            return jsonify(errors['AlreadyExistsError'])

        except NotMatchPasswordWithConfirmError:
            return jsonify(errors['NotMatchPasswordWithConfirmError'])

        except UnauthorizedError:
            return jsonify(errors['UnauthorizedError'])

        # return jsonify({
        #     "message": "Unsuccessful"
        # })


class SignUpEmployer(Resource):
    def post(self):
        try:
            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('first_name', type=str, required=True)
            parser.add_argument('last_name', type=str, required=True)
            parser.add_argument('username', type=str, required=True)
            parser.add_argument('password', type=str, required=True)
            parser.add_argument('confirm_password', type=str, required=True)

            args = parser.parse_args()

            if args['password'] != args['confirm_password']:
                raise NotMatchPasswordWithConfirmError

            if ('logged_in' in list(session.keys())) and session['logged_in']:
                raise AlreadyIsLoggedInError

            login_employer_info = login_employer(args['username'], args['password'])

            if is_found_user(login_employer_info):
                raise AlreadyExistsError

            add_employee = add_new_employer(
                args['first_name'],
                args['last_name'],
                args['password'],
                args['username']
            )

            if add_employee == -1:
                raise AlreadyExistsError

            return jsonify({
                "message": "Successful",
            })

        except AlreadyExistsError:
            return jsonify(errors['AlreadyExistsError'])

        except NotMatchPasswordWithConfirmError:
            return jsonify(errors['NotMatchPasswordWithConfirmError'])

        except UnauthorizedError:
            return jsonify(errors['UnauthorizedError'])


class LoginEmployee(Resource):
    def post(self):
        try:
            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, required=True)
            parser.add_argument('password', type=str, required=True)

            args = parser.parse_args()

            login_employee_info = login_employee(args['username'], args['password'])

            if is_found_user(login_employee_info):
                session['logged_in'] = True
                session['role'] = 'employee'
                session['username'] = login_employee_info[0][4]
                session['id'] = login_employee_info[0][0]
                # passing the username as an identifier
                access_token = create_access_token(identity=login_employee_info[0][4])

                return jsonify(access_token=access_token)

        except UnauthorizedError:
            return jsonify(errors['UnauthorizedError'])

        return jsonify({
            "message": "Unsuccessful"
        })


class LoginEmployer(Resource):
    def post(self):
        try:
            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, required=True)
            parser.add_argument('password', type=str, required=True)

            args = parser.parse_args()

            login_employer_info = login_employer(args['username'], args['password'])

            if is_found_user(login_employer_info):
                session['logged_in'] = True
                session['role'] = 'customer'
                session['username'] = login_employer_info[0][4]
                session['id'] = login_employer_info[0][0]
                access_token = create_access_token(identity=login_employer_info[0][4])
                return jsonify(access_token=access_token)
            else:
                raise UnauthorizedError
        except UnauthorizedError:
            return jsonify(errors['UnauthorizedError'])


class Logout(Resource):
    def post(self):
        try:
            if not ('logged_in' in list(session.keys())) or not session['logged_in']:
                raise NotExistsError
            role = session['role']
            username = session['username']
            id = session['id']

            print([role, username, id])
            session.clear()

            return jsonify({
                "message": "Successfully Logged Out",
                "role": role,
                "username": username,
                "id": id
            })

        except NotExistsError:
            return jsonify(errors['NotExistsError'])
