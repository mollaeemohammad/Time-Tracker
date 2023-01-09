from flask import jsonify
from flask_restful import Resource, reqparse
from utilities.delete_employee_from_project import delete_employee_from_project
from utilities.errors import *
from flask_jwt_extended import jwt_required, get_jwt_identity
from utilities.get_projects_of_employer import get_projects_of_employer


def is_in_projects(project_name: str, projects: list) -> bool:
    """
    The result of getting projects of an employer is comming in here
    as is determined that the provided project is in here or not.
    :param project_name:
    :param projects:
    :return:
    """
    for project in projects:
        if project[0] == project_name:
            return True
    return False


class DeleteEmployeeFromProject(Resource):
    @jwt_required()
    def post(self):
        try:
            """
                {
                    "project_name": str,
                    "employee_username": str
                }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('project_name', type=str, required=True)
            parser.add_argument('employee_username', type=str, required=True)
            args = parser.parse_args()

            project_name = args['project_name']
            employee_username = args['employee_username']
            employer_username = get_jwt_identity()

            projects = get_projects_of_employer(employer_username=employer_username)

            if not is_in_projects(project_name=project_name, projects=projects):
                raise DeletingError

            result_of_deletion = delete_employee_from_project(project_name=project_name,
                                                              employee_username=employee_username)

            if result_of_deletion == -1:
                raise DeletingError

            return jsonify({
                "message": "Successful",
            })

        except DeletingError:
            return jsonify(errors['DeletingError'])
