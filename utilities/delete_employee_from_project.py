from connection import conn
from mysql.connector import Error
from utilities.get_project import get_project
from utilities.get_employee import get_employee
from utilities.errors import NotExistsError


def delete_employee_from_project(project_name: str, employee_username: str) -> int:
    try:
        project = get_project(project_name)
        employee = get_employee(employee_username)
        if project is None or employee is None:
            raise NotExistsError
    except NotExistsError:
        return -1

    project_id = project[0]
    employee_id = employee[0]

    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM employee_projects AS ep \
                         WHERE ep.employee_id="{employee_id}" \
                         AND ep.project_id="{project_id}"')
        conn.commit()
        return cursor.rowcount
    except Error as error:
        print(error)
        return -1
