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

        cursor.execute(f'CREATE TABLE IF NOT EXISTS projects \
                            ( \
                                id            INT PRIMARY KEY AUTO_INCREMENT, \
                                description   TEXT, \
                                created_at    TIMESTAMP DEFAULT (CURRENT_TIMESTAMP), \
                                finished_date TIMESTAMP \
                            );')
        conn.commit()

        cursor.execute(f'CREATE TABLE IF NOT EXISTS hours \
                            ( \
                                project_id       INT NOT NULL, \
                                employee_id      INT NOT NULL, \
                                measured_hours   FLOAT NOT NULL, \
                                date_time        DATE DEFAULT (CURRENT_DATE), \
                                finished_date    TIMESTAMP, \
                                FOREIGN KEY (project_id) REFERENCES projects (id) \
                                    ON DELETE CASCADE \
                                    ON UPDATE CASCADE, \
                                FOREIGN KEY (employee_id) REFERENCES employee (id) \
                                    ON DELETE CASCADE \
                                    ON UPDATE CASCADE \
                            );')
        conn.commit()

        cursor.execute(f'CREATE TABLE IF NOT EXISTS employee_projects \
                            ( \
                                project_id       INT NOT NULL, \
                                employee_id      INT NOT NULL, \
                                FOREIGN KEY (project_id) REFERENCES projects (id) \
                                    ON DELETE CASCADE \
                                    ON UPDATE CASCADE, \
                                FOREIGN KEY (employee_id) REFERENCES employee (id) \
                                    ON DELETE CASCADE \
                                    ON UPDATE CASCADE \
                            );')
        conn.commit()

        cursor.execute(f'CREATE TABLE IF NOT EXISTS employer_projects \
                            ( \
                                project_id       INT NOT NULL, \
                                employer_id      INT NOT NULL, \
                                FOREIGN KEY (project_id) REFERENCES projects (id) \
                                    ON DELETE CASCADE \
                                    ON UPDATE CASCADE, \
                                FOREIGN KEY (employer_id) REFERENCES employer (id) \
                                    ON DELETE CASCADE \
                                    ON UPDATE CASCADE \
                            );')
        conn.commit()

        cursor.execute(f'CREATE TABLE IF NOT EXISTS images \
                            ( \
                                project_id       INT NOT NULL, \
                                employee_id      INT NOT NULL, \
                                employer_id      INT NOT NULL, \
                                date_time        DATE default (CURRENT_DATE), \
                                url              VARCHAR(500) NOT NULL, \
                                FOREIGN KEY (project_id) REFERENCES projects (id) \
                                    ON DELETE CASCADE \
                                    ON UPDATE CASCADE, \
                                FOREIGN KEY (employer_id) REFERENCES employer (id) \
                                    ON DELETE CASCADE \
                                    ON UPDATE CASCADE, \
                                FOREIGN KEY (employee_id) REFERENCES employee (id) \
                                    ON DELETE CASCADE \
                                    ON UPDATE CASCADE \
                            );')
        conn.commit()

    except Error as error:
        conn.rollback()
        print(error)
        return -1
