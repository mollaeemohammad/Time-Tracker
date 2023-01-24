from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from apis.update_description import employer_has_this_project
from utilities.errors import *
from utilities.update_project_status import update_project_status


class UpdateProjectStatus(Resource):
    @jwt_required()
    def post(self):
        try:
            """
                {
                    "project_name": str,
                    "new_status": str
                }
            """

            # Create a parser to parse arguments provided in the json
            parser = reqparse.RequestParser()
            parser.add_argument('project_name', type=str, required=True)
            parser.add_argument('new_status', type=str, required=True)
            args = parser.parse_args()

            project_name = args['project_name']
            new_status = args['new_status']
            employer_username = get_jwt_identity()

            if employer_has_this_project(employer_username, project_name) is False:
                raise NotAllowedToDoThis

            result_of_updating_status = update_project_status(project_name=project_name,
                                                              new_status=new_status)

            if result_of_updating_status == -1:
                raise UnableToAddToDataBase

            return jsonify({
                "message": "Successful",
            })

        except UnableToAddToDataBase:
            return jsonify(errors['UnableToAddToDataBase'])

        except NotAllowedToDoThis:
            return jsonify(errors['NotAllowedToDoThis'])
