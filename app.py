from datetime import timedelta
from flask import Flask, g, current_app
from flask_restful import Api
# from flask_rbac import RBAC, RoleMixin, UserMixin
from utilities.errors import errors
import logging
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from utilities.create_tables import create_tables
from apis.login import LoginEmployee, LoginEmployer, Logout, SignUpEmployee, SignUpEmployer
from apis.add_new_project import AddNewProject
from apis.update_description import UpdateDescriptionOfProject
from apis.delete_employee import DeleteEmployee
from apis.delete_employer import DeleteEmployer
from apis.delete_employee_from_project import DeleteEmployeeFromProject
from apis.delete_project import DeleteProject
from apis.get_employees_added_to_project import GetEmployeesAddedToProject
from apis.get_employee import GetEmployee
from apis.get_employer import GetEmployer
from apis.get_project import GetProject
from apis.get_projects_of_employee import GetProjectsOfEmployee
from apis.get_projects_of_employer import GetProjectsOfEmployer
from apis.update_project_status import UpdateProjectStatus
from apis.insert_hours import InsertHours
from apis.get_hours_of_employee import GetHoursOfEmployee
from apis.get_hours_of_all_employees import GetHoursOfAllEmployees
from apis.get_total_hours_of_employee import GetTotalHoursOfEmployee
from apis.update_fee import UpdateFee


def init_routes(api: Api) -> None:
    """
    Add API URL routes
    :param api: The Flask API object to which URLs are added
    """
    api.add_resource(LoginEmployee, '/api/login_employee')
    api.add_resource(LoginEmployer, '/api/login_employer')
    api.add_resource(SignUpEmployee, '/api/signup_employee')
    api.add_resource(SignUpEmployer, '/api/signup_employer')
    api.add_resource(Logout, '/api/logout')
    api.add_resource(AddNewProject, '/api/add_new_project')
    api.add_resource(UpdateDescriptionOfProject, '/api/update_description_of_project')
    api.add_resource(DeleteEmployee, '/api/delete_employee')
    api.add_resource(DeleteEmployer, '/api/delete_employer')
    api.add_resource(DeleteEmployeeFromProject, '/api/delete_employee_from_project')
    api.add_resource(DeleteProject, '/api/delete_project')
    api.add_resource(GetEmployeesAddedToProject, '/api/get_employees_added_to_project')
    api.add_resource(GetEmployee, '/api/get_employee')
    api.add_resource(GetEmployer, '/api/get_employer')
    api.add_resource(GetProject, '/api/get_project')
    api.add_resource(GetProjectsOfEmployee, '/api/get_projects_of_employee')
    api.add_resource(GetProjectsOfEmployer, '/api/get_projects_of_employer')
    api.add_resource(UpdateProjectStatus, '/api/update_project_status')
    api.add_resource(InsertHours, '/api/insert_hours')
    api.add_resource(GetHoursOfEmployee, '/api/get_hours_of_employee')
    api.add_resource(GetHoursOfAllEmployees, '/api/get_hours_of_all_employees')
    api.add_resource(GetTotalHoursOfEmployee, '/api/get_total_hours_of_employee')
    api.add_resource(UpdateFee, '/api/update_fee')


def create_app() -> Flask:
    """
    :return: The Flask object which will run and listen to incoming requests
    """
    app = Flask(__name__)
    # SqlAlchemy Database Configuration With Mysql
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:asd147''@localhost/time_tracker'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
    app.secret_key = 'asdsdfsdfs13sdf_df%&'

    # setting up the jwt extension
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(weeks=100)
    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
    jwt = JWTManager(app)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    log_handler = logging.FileHandler(filename='./logs/requests.log', mode='a+')
    formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s %(filename)s %(funcName)s %(message)s')
    log_handler.setFormatter(formatter)
    app.logger.addHandler(log_handler)

    # rbac.init_app(app)

    app.config['RBAC_USE_WHITE'] = True
    # app.config.update(
    #     SESSION_COOKIE_SECURE='True',
    #     SESSION_COOKIE_HTTPONLY=True,
    #     SESSION_COOKIE_SAMESITE='None'
    # )

    create_tables()

    # Create a Flask API object
    api = Api(app, errors=errors)
    # Initialize API routes
    init_routes(api)
    return app
