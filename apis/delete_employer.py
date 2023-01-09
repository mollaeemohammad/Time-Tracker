from flask import jsonify, session
from flask_restful import Resource, reqparse
from utilities.delete_employer import delete_employer
from utilities.errors import *
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class DeleteEmployer(Resource):
    @jwt_required()
    def post(self):
        try:
            employer_username = get_jwt_identity()

            result_of_deletion = delete_employer(username=employer_username)

            if result_of_deletion == -1:
                raise DeletingError

            return jsonify({
                "message": "Successful",
            })

        except DeletingError:
            return jsonify(errors['DeletingError'])

