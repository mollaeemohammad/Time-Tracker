from flask import Flask, g, current_app
from flask_restful import Api
# from flask_rbac import RBAC, RoleMixin, UserMixin
from utilities.errors import errors
import logging
from flask_cors import CORS
from utilities.create_tables import create_tables
from apis.login import LoginEmployee, LoginEmployer, Logout


def init_routes(api: Api) -> None:
    """
    Add API URL routes
    :param api: The Flask API object to which URLs are added
    """
    api.add_resource(LoginEmployee, '/api/login_employee')
    api.add_resource(LoginEmployer, '/api/login_employer')
    # api.add_resource(LoginAdmin, '/api/login_admin')
    # api.add_resource(LoginCustomer, '/api/login_customer')
    # api.add_resource(LoginStore, '/api/login_store')
    # api.add_resource(Logout, '/api/logout')
    # api.add_resource(AllCategories, '/api/all_categories')
    # api.add_resource(AllProductsOfCategory, '/api/all_products_of_category')
    # api.add_resource(SearchInProducts, '/api/search_in_products')
    # api.add_resource(AllStores, '/api/all_stores')
    # api.add_resource(ChooseProduct, '/api/choose_product')
    # api.add_resource(Buy, '/api/buy')
    # api.add_resource(AllAddressesOfCustomer, '/api/all_addresses_of_customer')
    # api.add_resource(UpdateProductCount, '/api/update_product_count')
    # api.add_resource(AddReview, '/api/add_review')
    # api.add_resource(AddNewProduct, '/api/add_new_product')
    # api.add_resource(AddProblem, '/api/add_problem')
    # api.add_resource(AllOrdersOfCustomer, '/api/all_orders_of_customer')
    # api.add_resource(AllProblemsOfStore, '/api/all_problems_of_store')
    # api.add_resource(ChooseOrder, '/api/choose_order')
    # api.add_resource(UpVote, '/api/up_vote')
    # api.add_resource(DownVote, '/api/down_vote')
    # api.add_resource(UpdateDiscountProductStore, '/api/update_discount_product_store')
    # api.add_resource(AllDeliveries, '/api/all_deliveries')
    # api.add_resource(AddNewCategory, '/api/add_new_category')
    # api.add_resource(AddNewCustomer, '/api/add_new_customer')
    # api.add_resource(AddNewStore, '/api/add_new_store')
    # api.add_resource(AddNewAddressToCustomer, '/api/add_new_address_to_customer')
    # api.add_resource(Suggestion, '/api/suggestion')
    # api.add_resource(UpdateStatusOrderCustomer, '/api/update_status_order_customer')


def create_app() -> Flask:
    """
    :return: The Flask object which will run and listen to incoming requests
    """
    app = Flask(__name__)
    # SqlAlchemy Database Configuration With Mysql
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:asd147''@localhost/time_tracker'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    app.secret_key = 'asdsdfsdfs13sdf_df%&'

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    log_handler = logging.FileHandler(filename='./logs/requests.log', mode='a+')
    formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s %(filename)s %(funcName)s %(message)s')
    log_handler.setFormatter(formatter)
    app.logger.addHandler(log_handler)

    # rbac.init_app(app)

    app.config['RBAC_USE_WHITE'] = True

    create_tables()

    # Create a Flask API object
    api = Api(app, errors=errors)
    # Initialize API routes
    init_routes(api)
    return app
