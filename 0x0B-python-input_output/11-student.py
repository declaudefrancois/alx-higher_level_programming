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

    def to_json(self, attrs=None):
        """Returns a dictionary representation of
        the object.

        Args:
            attrs(list|None): An optional list of attributes
                              to ignore.

        Returns:
            dict: The dictionary representation.
        """
        obj_dict = self.__dict__
        return {x: obj_dict[x] for x in obj_dict
                if attrs is None or x in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        from the json object.

        Args:
            json (dict): The new attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)
