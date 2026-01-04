#!/usr/bin/env python3
"""Pickle serialization module: serialize/deserialize Python objects."""

import pickle


class CustomObject:
    """A simple custom object for testing Pickle serialization."""

    def __init__(self, name, age, active):
        """
        Initialize CustomObject.

        Args:
            name (str): Name of the object
            age (int): Age of the object
            active (bool): Status flag
        """
        self.name = name
        self.age = age
        self.active = active

    def __repr__(self):
        return (
            f"<CustomObject name={self.name} "
            f"age={self.age} "
            f"active={self.active}>"
        )

    def display(self):
        """Print the object for visual inspection (used by tests)."""
        print(self)

    def serialize(self, filename):
        """Serialize this object to a file using Pickle."""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def deserialize(filename):
        """Load a Pickle file and return the object."""
        with open(filename, "rb") as f:
            return pickle.load(f)


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python object and save it to a file using Pickle.

    Args:
        data: Any Python object (dict, list, tuple, set, class instance, etc.)
        filename: Output file name
    """
    with open(filename, "wb") as f:  # wb → write binary
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a Pickle file and deserialize it into a Python object.

    Args:
        filename: Input Pickle file

    Returns:
        Python object loaded from the file
    """
    with open(filename, "rb") as f:  # rb → read binary
        return pickle.load(f)
