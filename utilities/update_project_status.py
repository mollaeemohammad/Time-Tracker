from connection import conn
from mysql.connector import Error


def update_project_status(project_name: str, new_status: str) -> int:
    try:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE projects \
                         SET status = "{new_status}" \
                         WHERE name="{project_name}"')
        conn.commit()
        return cursor.lastrowid
    except Error as error:
        print(error)
        return -1
