from utilities.get_employees_added_to_project import get_employees_added_to_project
from utilities.get_hours_of_employee import get_hours_of_employee


def get_hours_of_all_employees(project_name: str) -> dict:
    """
    Getting all working hours of all employees
    :param project_name:
    :return: dict
    """
    employees = get_employees_added_to_project(project_name=project_name)
    hours = {}
    for employee in employees:
        employee_username = employee[3]
        hours[employee_username] = get_hours_of_employee(employee_username=employee_username, project_name=project_name)
    return hours
