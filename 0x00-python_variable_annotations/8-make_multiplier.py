#!/usr/bin/env python3
"""type-annotated function that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a function that returns a function multiplies a float"""
    return lambda x: x * multiplier
