#!/usr/bin/env python3
"""a type-annotated function to give values with appropriate types"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a fuction that returns values with appropriate types"""
    return [(i, len(i)) for i in lst]
