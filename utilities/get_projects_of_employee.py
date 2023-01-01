from connection import conn
from mysql.connector import Error
from utilities.get_employee import get_employee


def get_projects_of_employee(employee_username: str) -> list:
    try:
        employee = get_employee(employee_username)
        employee_id = employee[0]
        cursor = conn.cursor()
        cursor.execute(f'SELECT p.name, p.description, p.created_at, p.created_at \
                         FROM employee_projects AS ep \
                         INNER JOIN projects AS p on ep.project_id = p.id \
                         WHERE ep.employee_id="{employee_id}"')
        return cursor.fetchall()
    except Error as error:
        print(error)
        return ["Something went wrong"]
