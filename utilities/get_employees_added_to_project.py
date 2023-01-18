from connection import conn
from mysql.connector import Error
from utilities.get_employee import get_employee
from utilities.get_project import get_project


def get_employees_added_to_project(project_name: str) -> list:
    try:
        project = get_project(project_name)
        projects_id = project[0]
        cursor = conn.cursor()
        cursor.execute(f'SELECT e.id, e.last_name, e.first_name, e.username, e.created_at \
                         FROM employee_projects AS ep \
                         INNER JOIN employee AS e on ep.employee_id = e.id \
                         WHERE ep.project_id="{projects_id}"')
        return cursor.fetchall()
    except Error as error:
        print(error)
        return ["Something went wrong"]
