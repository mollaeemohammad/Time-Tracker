from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from apis.update_description import employer_has_this_project
from utilities.errors import *
from utilities.insert_hours import insert_hours


class InsertHours(Resource):
    @jwt_required()
    def post(self):
        try:
            """
                {
                    "employee_username": "employee",
                    "project_name": "test",
                    "measured_hours": float
                }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('project_name', type=str, required=True)
            parser.add_argument('employee_username', type=str, required=True)
            parser.add_argument('measured_hours', type=float, required=True)
            args = parser.parse_args()

            project_name = args['project_name']
            employee_username = args['employee_username']
            measured_hours = args['measured_hours']
            employer_username = get_jwt_identity()

            if employer_has_this_project(employer_username=employer_username, project_name=project_name) is False:
                raise NotAllowedToDoThis

            result_of_adding_project = insert_hours(employee_username=employee_username,
                                                    project_name=project_name,
                                                    measured_hours=measured_hours)

            if result_of_adding_project == -1:
                raise UnableToAddToDataBase

            return jsonify({
                "message": "Successful",
            })

        except UnableToAddToDataBase:
            return jsonify(errors['UnableToAddToDataBase'])
        except NotAllowedToDoThis:
            return jsonify(errors['NotAllowedToDoThis'])
