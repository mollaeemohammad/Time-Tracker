from connection import conn
from mysql.connector import Error
from utilities.get_employee import get_employee
from utilities.get_project import get_project
from utilities.errors import NotExistsError, errors


def add_employee_to_project(employee_username: str, project_name: str) -> int:
    try:
        employee = get_employee(employee_username)
        project = get_project(project_name)
        if employee is None or project is None:
            raise NotExistsError
    except NotExistsError:
        return -1

    try:
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO employee_projects (project_id, employee_id) \
                        VALUES ("{project[0]}", "{employee[0]}")')
        conn.commit()
        return cursor.lastrowid
    except Error as error:
        print(error)
        return -1
