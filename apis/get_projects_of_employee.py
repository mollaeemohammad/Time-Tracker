from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from utilities.get_projects_of_employee import get_projects_of_employee


class GetProjectsOfEmployee(Resource):
    @jwt_required()
    def get(self):
        try:
            employee_username = get_jwt_identity()

            return jsonify(get_projects_of_employee(employee_username=employee_username))

        except:
            return jsonify({
                "message": "Something went wrong",
                "status": 503
            })
