#!/usr/bin/env python3
'''async gather function'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''executes 4 function asynchronously'''
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(), async_comprehension(),
        async_comprehension(), async_comprehension()
    )

    return time.time() - start_time
