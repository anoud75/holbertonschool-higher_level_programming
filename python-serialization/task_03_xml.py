#!/usr/bin/python3
"""This module provides XML serialization and deserialization functions."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary: A Python dictionary to serialize.
        filename: The filename to save the XML data to.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="unicode")


def deserialize_from_xml(filename):
    """Deserialize an XML file to a Python dictionary.

    Args:
        filename: The filename to read the XML data from.

    Returns:
        A Python dictionary with the deserialized XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
