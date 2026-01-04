#!/usr/bin/env python3
"""Pickle serialization module: serialize/deserialize Python objects."""

import pickle

class CustomObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"<CustomObject name={self.name} value={self.value}>"

def serialize_and_save_to_file(data, filename):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def load_and_deserialize(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
