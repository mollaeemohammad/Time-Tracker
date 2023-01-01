from connection import conn
from mysql.connector import Error


def get_employer(username: str) -> list:
    try:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM employer AS p WHERE p.username="{username}"')
        return cursor.fetchone()
    except Error as error:
        print(error)
        return ['Something went wrong']
