from connection import conn
from mysql.connector import Error
from utilities.add_new_project import add_new_project
from utilities.errors import AlreadyExistsError
from utilities.get_employer import get_employer


def add_new_project_by_employer(employer_username: str, name: str, description: str) -> int:
    try:
        cursor = conn.cursor()
        project_id = add_new_project(name=name, description=description)
        if project_id == -1:
            raise AlreadyExistsError

        employer = get_employer(username=employer_username)

        employer_id = employer[0]

        cursor.execute(f'INSERT INTO employer_projects (project_id, employer_id) \
                        VALUES ("{project_id}", "{employer_id}")')
        conn.commit()

        return cursor.lastrowid
    except AlreadyExistsError:
        return -1
    except Error as error:
        print(error)
        return -1
