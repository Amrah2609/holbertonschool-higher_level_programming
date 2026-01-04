#!/usr/bin/python3
"""Defines a Student class with filtered JSON serialization."""


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
