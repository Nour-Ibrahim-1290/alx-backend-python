#!/usr/bin/env python3
""" Async Operations"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
         an asynchronous coroutine that takes in an integer argument
         (max_delay, with a default value of 10) named wait_random
         that waits for a random delay between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
