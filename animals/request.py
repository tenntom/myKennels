ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
    },
    {
        "id": 4,
        "name": "Spot",
        "breed": "Beagle",
        "customerId": 5,
        "locationId": 2
    },
    {
        "id": 5,
        "name": "Dudley",
        "breed": "Bulldog",
        "customerId": 1,
        "locationId": 2
    },
    {
        "id": 6,
        "name": "Sadie",
        "breed": "Cocker Spaniel",
        "customerId": 2,
        "locationId": 1
    },
    {
        "name": "Sparky",
        "breed": "Beagle",
        "locationId": 1,
        "customerId": 4,
        "id": 7
    },
    {
        "id": 8,
        "name": "Jimmy",
        "locationId": 1,
        "customerId": 1
    },
    {
        "name": "Sparkle Kitten",
        "locationId": 1,
        "customerId": 3,
        "id": 9
    },
    {
        "id": 10,
        "name": "Doodles",
        "breed": "Poodle",
        "customerId": 3,
        "locationId": 2
    },
    {
        "id": 11,
        "name": "Pickles",
        "breed": "Chihuahua",
        "customerId": 4,
        "locationId": 1
    }
]


def get_all_animals():
    """Gets the list of animals"""
    return ANIMALS


def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal


def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal

def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)