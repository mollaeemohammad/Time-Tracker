from connection import conn
from mysql.connector import Error
from utilities.get_project import get_project
from utilities.get_employee import get_employee


def get_hours_of_employee(employee_username: str, project_name: str) -> list:
    try:
        cursor = conn.cursor()
        employee = get_employee(username=employee_username)
        project = get_project(name=project_name)
        cursor.execute(f'SELECT * FROM hours AS h WHERE h.project_id="{project[0]}" AND h.employee_id="{employee[0]}"')
        return cursor.fetchall()
    except Error as error:
        print(error)
        return ['Something went wrong']
