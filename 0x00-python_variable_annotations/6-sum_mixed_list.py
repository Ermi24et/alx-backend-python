#!/usr/bin/env python3
"""type-annotated function that gives a sum of floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a function that returns sum of mixed lists as a float"""
    return sum(mxd_lst)
