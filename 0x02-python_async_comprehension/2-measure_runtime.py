#!/usr/bin/env python3
"""
a module for run time four parallel comrehensions
"""
from asyncio import gather
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    a coroutine that will execute async comprehension
    """
    initial_time = time.perf_counter()
    await gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - initial_time
