from connection import conn
from mysql.connector import Error
from utilities.get_employee import get_employee
from utilities.get_project import get_project


def get_fee(employee_username: str, project_name: str) -> list:
    try:
        employee = get_employee(employee_username)
        project = get_project(project_name)
        cursor = conn.cursor()
        cursor.execute(
            f'SELECT ep.fee FROM employee_projects AS ep WHERE employee_id="{employee[0]}" AND project_id="{project[0]}"')
        return cursor.fetchone()
    except Error as error:
        print(error)
        return ["Something went wrong"]
