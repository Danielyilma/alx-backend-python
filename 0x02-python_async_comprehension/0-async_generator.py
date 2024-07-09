#!/usr/bin/env python3
'''async generator'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, float]:
    '''generates random float asynchronously from 0-10'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
