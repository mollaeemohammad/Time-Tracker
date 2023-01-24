from connection import conn
from mysql.connector import Error


def get_employee(username: str) -> list:
    try:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM employee AS p WHERE p.username="{username}"')
        return cursor.fetchone()
    except Error as error:
        print(error)
        return ["Something went wrong"]
