EMPLOYEES = [
    {
      "id": 1,
      "name": "Bob Saget",
      "position": "General Manager",
      "locationId": 1,
      "payRate": 15
    },
    {
      "id": 2,
      "name": "Punky Brewster",
      "position": "Dog Groomer",
      "locationId": 2,
      "payRate": 15
    },
    {
      "id": 3,
      "name": "Willis Jackson ",
      "position": "Sales Manager",
      "locationId": 1,
      "payRate": 15
    },
    {
      "id": 4,
      "name": "Blair",
      "position": "Interior Designer",
      "locationId": 2,
      "payRate": 15
    },
    {
      "name": "Mike Sevier",
      "locationId": 2,
      "position": "Janitor",
      "id": 5,
      "payRate": 15
    },
    {
      "name": "Marcia Brady",
      "locationId": 2,
      "position": "Marketing Assistant",
      "id": 6,
      "payRate": 15
    }
]


def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
    

def create_employee(employee):

    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)
    
    return employee

def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break