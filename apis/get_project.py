from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from apis.update_description import employer_has_this_project
from utilities.errors import *
from utilities.get_project import get_project


class GetProject(Resource):
    @jwt_required()
    def get(self):
        try:
            """
                {
                    "project_name": str,
                }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('project_name', type=str, required=True)
            args = parser.parse_args()

            project_name = args['project_name']
            employer_username = get_jwt_identity()

            if employer_has_this_project(employer_username, project_name) is False:
                raise NotAllowedToDoThis

            return jsonify(get_project(name=project_name))

        except NotAllowedToDoThis:
            return jsonify(errors['NotAllowedToDoThis'])
