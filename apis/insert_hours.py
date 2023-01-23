from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from apis.update_description import employee_has_this_project
from utilities.errors import *
from utilities.insert_hours import insert_hours


class InsertHours(Resource):
    @jwt_required()
    def post(self):
        try:
            """
                {
                    "project_name": "test",
                    "measured_hours": float
                }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('project_name', type=str, required=True)
            parser.add_argument('measured_hours', type=float, required=True)
            args = parser.parse_args()

            project_name = args['project_name']
            measured_hours = args['measured_hours']
            employee_username = get_jwt_identity()

            if employee_has_this_project(employee_username=employee_username, project_name=project_name) is False:
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
