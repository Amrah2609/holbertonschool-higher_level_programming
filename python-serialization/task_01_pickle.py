#!/usr/bin/env python3
"""Pickle serialization module: serialize/deserialize Python objects."""

import pickle


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
