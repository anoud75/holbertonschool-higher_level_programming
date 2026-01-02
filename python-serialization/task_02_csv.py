#!/usr/bin/python3
"""This module converts CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and save to data.json.

    Args:
        csv_filename: The filename of the CSV file to convert.

    Returns:
        True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
