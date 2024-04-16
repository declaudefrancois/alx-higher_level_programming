#!/usr/bin/python3
"""Define the Student class.
"""


class Student:
    """Represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """Instantiate a new student.

        Args:
            first_name (str): The student's firstname.
            last_name (Str): The student's lastname.
            age (int) The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of
        the object.

        Returns:
            dict: The dictionary representation.
        """
        return self.__dict__
