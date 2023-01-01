from connection import conn
from mysql.connector import Error


def delete_employee(username: str) -> int:
    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM employee AS p WHERE p.username="{username}"')
        conn.commit()
        return cursor.rowcount
    except Error as error:
        print(error)
        return -1
