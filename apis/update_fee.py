from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from apis.update_description import employer_has_this_project
from utilities.errors import *
from utilities.update_project_status import update_project_status
from utilities.update_fee import update_fee


class UpdateFee(Resource):
    @jwt_required()
    def post(self):
        try:
            """
            {
                "project_name": str,
                "employee_username": str,
                'new_fee': float
            }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('project_name', type=str, required=True)
            parser.add_argument('employee_username', type=str, required=True)
            parser.add_argument('new_fee', type=float, required=True)
            args = parser.parse_args()

            project_name = args['project_name']
            employee_username = args['employee_username']
            new_fee = args['new_fee']

            employer_username = get_jwt_identity()

            if employer_has_this_project(employer_username, project_name) is False:
                raise NotAllowedToDoThis

            result_of_updating_fee = update_fee(project_name=project_name,
                                                employee_username=employee_username,
                                                new_fee=new_fee)

            if result_of_updating_fee == -1:
                raise UnableToAddToDataBase

            return jsonify({
                "message": "Successful",
            })

        except UnableToAddToDataBase:
            return jsonify(errors['UnableToAddToDataBase'])

        except NotAllowedToDoThis:
            return jsonify(errors['NotAllowedToDoThis'])
