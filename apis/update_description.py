from flask import jsonify, session
from flask_restful import Resource, reqparse
from utilities.update_description import update_description
from utilities.get_projects_of_employer import get_projects_of_employer
from utilities.get_projects_of_employee import get_projects_of_employee
from utilities.errors import *
from utilities.new_user import add_new_employee, add_new_employer
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


def employer_has_this_project(employer_username: str, project_name: str) -> bool:
    """
    Determines that the requested employer has the project or not
    :param employer_username:
    :param project_name:
    :return: bool
    """
    projects_of_employer = get_projects_of_employer(employer_username=employer_username)

    for project in projects_of_employer:
        if project[0] == project_name:
            return True

    return False

def employee_has_this_project(employee_username: str, project_name: str) -> bool:
    """
    Determines that the requested employee has the project or not
    :param employee_username:
    :param project_name:
    :return: bool
    """
    projects_of_employee = get_projects_of_employee(employee_username=employee_username)

    for project in projects_of_employee:
        if project[0] == project_name:
            return True

    return False


class UpdateDescriptionOfProject(Resource):
    @jwt_required()
    def post(self):
        try:
            """
                {
                    "project_name": str,
                    "new_description": str
                }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('project_name', type=str, required=True)
            parser.add_argument('new_description', type=str, required=True)
            args = parser.parse_args()

            project_name = args['project_name']
            new_description = args['new_description']
            employer_username = get_jwt_identity()

            if employer_has_this_project(employer_username, project_name) is False:
                raise NotAllowedToDoThis

            result_of_updating_description = update_description(project_name=project_name,
                                                                new_description=new_description)

            if result_of_updating_description == -1:
                raise UnableToAddToDataBase

            return jsonify({
                "message": "Successful",
            })

        except UnableToAddToDataBase:
            return jsonify(errors['UnableToAddToDataBase'])

        except NotAllowedToDoThis:
            return jsonify(errors['NotAllowedToDoThis'])
