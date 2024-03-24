#!/usr/bin/env python3
"""
a duck-typed annotations
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    correcting a function with the correct duck-typed annotation
    """
    if lst:
        return lst[0]
    else:
        return None
