from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from utilities.errors import *
from utilities.get_hours_of_employee import get_hours_of_employee
from utilities.get_fee import get_fee


def calculate_hours(hours: list) -> float:
    """
    Except of summing the hours in bellow API, I do it in here
    :param hours: A list of tuples with schema in hours table
    :return:
    """
    hours_amount = 0.0
    for hour in hours:
        hours_amount += hour[2]

    return hours_amount


class GetTotalHoursOfEmployee(Resource):
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

            hours = get_hours_of_employee(employee_username=employee_username, project_name=project_name)
            fee = get_fee(employee_username=employee_username, project_name=project_name)
            return jsonify({
                'total_hours': calculate_hours(hours=hours),
                'fee': fee
            })

        except NotAllowedToDoThis:
            return jsonify(errors['NotAllowedToDoThis'])
