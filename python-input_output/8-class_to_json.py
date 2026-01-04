#!/usr/bin/python3
"""Returns the dictionary description for JSON serialization of an object."""


def class_to_json(obj):
    """Return a dictionary of simple data structure attributes."""
    return obj.__dict__
