import datetime
import time
from mysql.connector import Error
from connection import conn
from utilities.errors import NotExistsError
from utilities.get_employee import get_employee
from utilities.get_project import get_project


def insert_hours(employee_username: str, project_name: str, measured_hours: float) -> int:
    try:
        employee = get_employee(employee_username)
        project = get_project(project_name)
        if employee is None or project is None:
            raise NotExistsError
    except NotExistsError:
        return -1

    try:
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO hours (project_id, employee_id, measured_hours, finished_time) \
                        VALUES ("{project[0]}", "{employee[0]}", "{measured_hours}", "{timestamp}")')
        conn.commit()
        return cursor.lastrowid
    except Error as error:
        print(error)
        return -1
