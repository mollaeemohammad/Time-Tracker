from connection import conn
from mysql.connector import Error


def add_new_project(name: str, description: str) -> int:
    try:
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO projects (name, description) \
                        VALUES ("{name}", "{description}")')
        conn.commit()
        return cursor.lastrowid
    except Error as error:
        print(error)
        return -1

