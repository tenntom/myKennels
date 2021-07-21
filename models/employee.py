class Employee():
    """Creates new employees"""
    def __init__(self, id, name, position, location_id):
        self.id = id
        self.name = name
        self.position = position
        self.location_id = location_id
        self.location = None
        
