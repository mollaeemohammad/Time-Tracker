from connection import conn
from mysql.connector import Error


def update_description(project_name: str, new_description: str) -> int:
    try:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE projects \
                         SET description= "{new_description}" \
                         WHERE name="{project_name}"')
        conn.commit()
        return cursor.lastrowid
    except Error as error:
        print(error)
        return -1
