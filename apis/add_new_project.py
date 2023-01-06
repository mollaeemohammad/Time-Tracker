from flask import jsonify, session
from flask_restful import Resource, reqparse
from utilities.add_new_project_by_employer import add_new_project_by_employer
from utilities.errors import *
from utilities.new_user import add_new_employee, add_new_employer
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class AddNewProject(Resource):
    @jwt_required()
    def post(self):
        try:
            """
                {
                    "project_name": str,
                    "description": str
                }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('project_name', type=str, required=True)
            parser.add_argument('description', type=str, required=True)
            args = parser.parse_args()

            project_name = args['project_name']
            description = args['description']
            employer_username = get_jwt_identity()

            result_of_adding_project = add_new_project_by_employer(employer_username=employer_username,
                                                                   name=project_name,
                                                                   description=description)

            if result_of_adding_project == -1:
                raise UnableToAddToDataBase

            return jsonify({
                "message": "Successful",
            })

        except UnableToAddToDataBase:
            return jsonify(errors['UnableToAddToDataBase'])

