from flask import jsonify, session
from flask_restful import Resource, reqparse
from utilities.update_description import update_description
from utilities.get_projects_of_employer import get_projects_of_employer
from utilities.errors import *
from utilities.new_user import add_new_employee, add_new_employer
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from apis.update_description import employer_has_this_project
from utilities.get_employees_added_to_project import get_employees_added_to_project


class GetEmployeesAddedToProject(Resource):
    @jwt_required()
    def get(self):
        try:
            """
                {
                    "project_name": str,
                }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('project_name', type=str, required=True)
            args = parser.parse_args()

            project_name = args['project_name']
            employer_username = get_jwt_identity()

            if employer_has_this_project(employer_username, project_name) is False:
                raise NotAllowedToDoThis

            return jsonify(get_employees_added_to_project(project_name=project_name))

        except NotAllowedToDoThis:
            return jsonify(errors['NotAllowedToDoThis'])
