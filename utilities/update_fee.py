from connection import conn
from mysql.connector import Error
from utilities.get_project import get_project
from utilities.get_employee import get_employee


def update_fee(project_name: str, employee_username: str, new_fee: float) -> int:
    try:

        project = get_project(project_name)
        employee = get_employee(employee_username)

        cursor = conn.cursor()
        cursor.execute(f'UPDATE employee_projects \
                         SET fee= "{new_fee}" \
                         WHERE project_id="{project[0]}" AND employee_id="{employee[0]}"')
        conn.commit()
        return cursor.lastrowid
    except Error as error:
        print(error)
        return -1
