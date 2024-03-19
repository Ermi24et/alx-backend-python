#!/usr/bin/env python3
"""
a module that contains coroutine
"""
import asyncio
import random


async def async_generator():
    """
    a coroutine that yields a random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
