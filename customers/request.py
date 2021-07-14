CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct",
      "active": True
    },
    {
      "id": 2,
      "name": "Jimmy Johnson",
      "address": "7002 Main Street",
      "active": True
    },
    {
      "id": 3,
      "name": "Bobby Bones",
      "address": "7002 Elm Street",
      "active": True
    },
    {
      "id": 4,
      "name": "Ginger George",
      "address": "7002 Park Ave",
      "active": True
    },
    {
      "id": 5,
      "name": "Larry Linklater",
      "address": "7002 Palisades Place",
      "active": True
    }
]


def get_all_customers():
    """Gets Customers"""
    return CUSTOMERS


def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):

    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)
    
    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break