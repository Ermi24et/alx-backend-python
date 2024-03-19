#!/usr/bin/env python3
"""
a module of coroutine
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    a coroutine that uses async comprehension over async generator
    """
    return [n async for n in async_generator()]
