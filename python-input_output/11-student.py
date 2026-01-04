#!/usr/bin/python3
"""Defines a Student class with JSON reload capability."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of the Student.
        If attrs is a list of strings, only those attributes are returned.
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        using a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
