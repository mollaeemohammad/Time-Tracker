from connection import conn
from mysql.connector import Error


def delete_project(name: str) -> int:
    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM projects AS p WHERE p.name="{name}"')
        conn.commit()
        return cursor.rowcount
    except Error as error:
        print(error)
        return -1
