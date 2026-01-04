#!/usr/bin/env python3
"""Serialize and deserialize Python dictionary to/from XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The input dictionary to serialize
        filename (str): The output XML filename
    """
    # Root element
    root = ET.Element("data")

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert all values to string

    # Write the XML tree to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The XML file to read

    Returns:
        dict: Python dictionary reconstructed from XML
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            # XML stores everything as string, so keep it as string
            result[child.tag] = child.text

        return result
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except ET.ParseError:
        print(f"Error: Failed to parse XML file '{filename}'.")
        return {}
