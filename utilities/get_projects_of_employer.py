from connection import conn
from mysql.connector import Error
from utilities.get_employer import get_employer


def get_projects_of_employer(employer_username: str) -> list:
    try:
        employee = get_employer(employer_username)
        employee_id = employee[0]
        cursor = conn.cursor()
        cursor.execute(f'SELECT p.name, p.description, p.created_at, p.created_at \
                         FROM employer_projects AS ep \
                         INNER JOIN projects AS p on ep.project_id = p.id \
                         WHERE ep.employer_id="{employee_id}"')
        return cursor.fetchall()
    except Error as error:
        print(error)
        return ["Something went wrong"]
