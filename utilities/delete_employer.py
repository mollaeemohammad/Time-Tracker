from connection import conn
from mysql.connector import Error


def delete_employer(username: str) -> int:
    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM employer AS p WHERE p.username="{username}"')
        conn.commit()
        return cursor.rowcount
    except Error as error:
        print(error)
        return -1
