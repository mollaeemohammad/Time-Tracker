from flask import jsonify
from flask_restful import Resource
from utilities.delete_employee import delete_employee
from utilities.errors import *
from flask_jwt_extended import jwt_required, get_jwt_identity


class DeleteEmployee(Resource):
    @jwt_required()
    def post(self):
        try:
            employer_username = get_jwt_identity()

            result_of_deletion = delete_employee(username=employer_username)

            if result_of_deletion == -1:
                raise DeletingError

            return jsonify({
                "message": "Successful",
            })

        except DeletingError:
            return jsonify(errors['DeletingError'])

