# Student: Maria Navarro
# Date: 2023-11-17
# Class: Python II - HW 1
class Person:
    """
    A class that represents a person with a name and a university_id (id)

    Attributes:
        name (str): The name of the student
        u_id (int): The university ID for the student

    Methods:
        __init__(name, u_id): Initializes a new Person instance
        __eq__(other): Checks if two Person objects are equal based on their u_id
        __ne__(other): Checks if two Person objects are not equal based on their u_id
        __str__(): Returns a string representation of the Person object.
    """
    def __init__(self, name, u_id):
        self.name = name
        self.u_id = u_id

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.u_id == other.u_id
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f'{self.name}: {self.u_id}'