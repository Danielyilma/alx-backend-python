#!/usr/bin/env python3
'''concurency with loop'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''calles async function n times with max_delay'''
    result = []

    for i in range(n):
        temp = await task_wait_random(max_delay)
        result.append(temp)
    return sorted(result)
