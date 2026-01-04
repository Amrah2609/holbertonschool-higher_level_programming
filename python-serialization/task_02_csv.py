#!/usr/bin/env python3
"""Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON and save it as 'data.json'.

    Args:
        csv_filename (str): The input CSV file name.

    Returns:
        bool: True if successful, False if any error occurs.
    """
    try:
        data_list = []

        # Open CSV file and read it as dictionaries
        with open(csv_filename, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        # Serialize to JSON and save
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
