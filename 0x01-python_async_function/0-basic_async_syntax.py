#!/usr/bin/env python3
"""
asynchronous coroutine
"""
import asyncio
import random
import time


async def wait_random(max_delay: float = 10):
    initia = time.perf_counter()
    await asyncio.sleep(random.randint(0, max_delay))
    elapsed = time.perf_counter() - initia
    return elapsed
