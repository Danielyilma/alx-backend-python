#!/usr/bin/env python3
'''async comprehension'''
import asyncio
from typing import AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, float]:
    '''implements async comprehension'''
    return [i async for i in async_generator()]
