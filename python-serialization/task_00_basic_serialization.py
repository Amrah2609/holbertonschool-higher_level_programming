#!/usr/bin/env python3
"""Basic serialization module: serialize Python dict to JSON and back."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The output file name.
    """
    with open(filename, "w") as f:  # 'w' → write (overwrite if file exists)
        json.dump(data, f)  # write dictionary as JSON into file


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.

    Args:
        filename (str): The JSON file to read from.

    Returns:
        dict: The Python dictionary loaded from the JSON file.
    """
    with open(filename, "r") as f:  # 'r' → read
        return json.load(f)  # read JSON from file and convert to Python dict
