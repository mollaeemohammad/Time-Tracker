from connection import conn
from mysql.connector import Error


def create_tables():
    try:
        cursor = conn.cursor()

        cursor.execute(f'CREATE TABLE IF NOT EXISTS employee \
                        ( \
                            id         INT PRIMARY KEY AUTO_INCREMENT, \
                            last_name  VARCHAR(300) NOT NULL, \
                            first_name VARCHAR(300) NOT NULL, \
                            password   VARCHAR(300) NOT NULL, \
                            username   VARCHAR(300) UNIQUE, \
                            created_at DATE DEFAULT (CURRENT_DATE) \
                        );')
        conn.commit()

        cursor.execute(f'CREATE TABLE IF NOT EXISTS employer \
                                ( \
                                    id         INT PRIMARY KEY AUTO_INCREMENT, \
                                    last_name  VARCHAR(300) NOT NULL, \
                                    first_name VARCHAR(300) NOT NULL, \
                                    password   VARCHAR(300) NOT NULL, \
                                    username   VARCHAR(300) UNIQUE, \
                                    created_at DATE DEFAULT (CURRENT_DATE) \
                                );')
        conn.commit()

    except Error as error:
        conn.rollback()
        print(error)
        return -1
