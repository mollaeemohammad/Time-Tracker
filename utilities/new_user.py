from connection import conn
from mysql.connector import Error


def add_new_employee(first_name: str, last_name: str, password: str, username: str) -> int:
    try:
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO employee (last_name, first_name, password, username) \
                        VALUES ("{last_name}", "{first_name}", "{password}", "{username}")')
        conn.commit()
        return cursor.lastrowid
    except Error as error:
        print(error)
        return -1


def add_new_employer(first_name: str, last_name: str, password: str, username: str) -> int:
    try:
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO employer (last_name, first_name, password, username) \
                        VALUES ("{last_name}", "{first_name}", "{password}", "{username}")')
        conn.commit()
        return cursor.lastrowid
    except Error as error:
        print(error)
        return -1
