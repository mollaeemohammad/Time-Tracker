from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from utilities.errors import *
from utilities.get_employer import get_employer
from utilities.get_hours_of_employee import get_hours_of_employee


class GetHoursOfEmployee(Resource):
    @jwt_required()
    def get(self):
        try:
            """
            {
                "employee_username": str,
                'project_name': str
            }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('employee_username', type=str, required=True)
            parser.add_argument('project_name', type=str, required=True)
            args = parser.parse_args()

            employee_username = args['employee_username']
            project_name = args['project_name']

            return jsonify(get_hours_of_employee(employee_username=employee_username, project_name=project_name))

        except:
            return jsonify(errors['NotAllowedToDoThis'])
