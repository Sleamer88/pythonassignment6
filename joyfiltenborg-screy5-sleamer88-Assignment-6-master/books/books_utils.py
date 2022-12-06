"""
XB_0082: Bestselling Books
Author: Emanuela Dumitru

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

import os


def get_absolute_path(relative_path: str) -> str:
    """
    Returns the absolute path of a path relative to the project's
    root.
    :param relative_path: path relative to the project's root
    :return: absolute path of the file/folder
    """
    current = os.path.dirname(__file__)
    parent = os.path.join(current, os.pardir)
    return os.path.join(os.path.abspath(parent), relative_path)
