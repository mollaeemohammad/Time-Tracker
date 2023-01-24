from connection import conn
from mysql.connector import Error


def login_employee(username: str, password: str) -> list:
    try:
        cursor = conn.cursor()
        cursor.execute(
            f'SELECT * \
             FROM employee \
             WHERE username = "{username}" AND password = "{password}";'
        )
        return cursor.fetchall()
    except Error as error:
        print(error)
        return ['Something went wrong']


def login_employer(username: str, password: str):
    try:
        cursor = conn.cursor()
        cursor.execute(
            f'SELECT * \
                FROM employer \
                WHERE username = "{username}" AND password = "{password}";'
        )
        return cursor.fetchall()
    except Error as error:
        print(error)
        return ['Something went wrong']
