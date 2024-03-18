#!/usr/bin/env python3
"""
asynchronous coroutine
"""
import asyncio
import random
import time


async def wait_random(max_delay: float = 10):
    """
    asynchronous coroutine that takes an argument and return
    random delay in seconds
    """
    initia: float = time.perf_counter()
    await asyncio.sleep(random.randint(0, max_delay))
    elapsed: float = time.perf_counter() - initia
    return elapsed
