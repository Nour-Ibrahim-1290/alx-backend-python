#!/usr/bin/env python3
""" Async Operations"""


import asyncio
import random


async def async_generator():
    """Generate 10 random numbers from 0 to 10
        waititng 1 secound at a time.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
