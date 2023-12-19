from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    all_employees = Employee.get_all()
    for employee in all_employees:
        print(employee)


def find_employee_by_name():
    name_ = input("Enter employee name to find: ")
    employee = Employee.find_by_name(name_)
    print(employee) if employee else print(
    f'Employee {name_} not found')



def find_employee_by_id():
    id_ = input("Enter employee id to find: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(
    f'Employee ID: {id_} not found')

#name, job_title, department_id
def create_employee():
    name_ = input("Enter the Employee's name: ")
    job_title_ = input("Enter the Employee's job_title: ")
    department_id_ = input("Enter the Employee department_id: ")
    try:
        employee = Employee.create(name_, job_title_, int(department_id_))
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    id = input("Enter Employee id: ")
    if updated_employee := Employee.find_by_id(id):
        try:
            name_ = input("Enter Employee name: ")
            updated_employee.name = name_

            job_title_ = input("Enter Employee job_title: ")
            updated_employee.job_title = job_title_

            department_id_ = input("Enter Employee department_id: ")
            updated_employee.department_id = int(department_id_)

            updated_employee.update()
            print("Employee update successful")
        except Exception as exc:
            print("Error updating employee, ", exc)
    else:
        print("Error: Employee not found")



def delete_employee():
    id = input("Enter Employee id: ")
    if employee := Employee.find_by_id(id):
        employee.delete()
        print(f"Employee {id} deletion successful")
    else:
        print(f"Employee {id} not found")


def list_department_employees():
    department_id = input("Enter department id: ")
    if department := Department.find_by_id(department_id):
        employees = department.employees()
        [print(f"{employee} \n") for employee in employees]
    else:
        print(f"Department {id} not found")