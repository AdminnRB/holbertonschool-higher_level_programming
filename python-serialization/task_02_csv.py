#!/usr/bin/env python3
"""Convert CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(filename):
    """Read the CSV file and write its rows to data.json.

    Returns True on success, False if the file is not found.
    """
    try:
        with open(filename, "r", newline="") as csv_file:
            data = list(csv.DictReader(csv_file))
    except FileNotFoundError:
        return False

    with open("data.json", "w") as json_file:
        json.dump(data, json_file)
    return True
