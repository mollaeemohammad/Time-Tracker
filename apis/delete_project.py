from flask import jsonify, session
from flask_restful import Resource, reqparse
from utilities.delete_project import delete_project
from utilities.errors import *
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from apis.update_description import employer_has_this_project


class DeleteProject(Resource):
    @jwt_required()
    def post(self):
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
            # employer_username = get_jwt_identity()
            #
            # if employer_has_this_project(employer_username, project_name) is False:
            #     raise NotAllowedToDoThis

            result_of_deletion = delete_project(name=project_name)

            if result_of_deletion == -1:
                raise DeletingError

            return jsonify({
                "message": "Successful",
            })

        except DeletingError:
            return jsonify(errors['DeletingError'])

