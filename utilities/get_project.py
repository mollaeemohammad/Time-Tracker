from connection import conn
from mysql.connector import Error


def get_project(name: str) -> list:
    try:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM projects AS p WHERE p.name="{name}"')
        return cursor.fetchone()
    except Error as error:
        print(error)
        return ["Something went wrong"]
