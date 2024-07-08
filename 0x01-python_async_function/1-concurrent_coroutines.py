#!/usr/bin/env python3
'''concurency with loop'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    '''calles async function n times with max_delay'''
    result = []

    for i in range(n):
        temp = await wait_random(max_delay)
        result.append(temp)
    return sorted(result)
