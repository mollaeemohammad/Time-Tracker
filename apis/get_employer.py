from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from utilities.errors import *
from utilities.get_employer import get_employer


class GetEmployer(Resource):
    @jwt_required()
    def get(self):
        try:
            """
                {
                    "username": str
                }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, required=True)
            args = parser.parse_args()

            username = args['username']

            return jsonify(get_employer(username=username))

        except:
            return jsonify(errors['NotAllowedToDoThis'])
