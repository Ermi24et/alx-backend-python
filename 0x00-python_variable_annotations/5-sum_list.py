#!/usr/bin/env python3
"""type-annotated function gives sum of arguments"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """a functon that returns a sum of list as a float"""
    return sum(input_list)
