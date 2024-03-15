#!/usr/bin/env python3
"""type-annotated function that returns a tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a function that returns a tuple"""
    return (k, v**2)
