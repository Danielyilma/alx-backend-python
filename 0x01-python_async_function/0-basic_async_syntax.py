#!/usr/bin/env python3
'''async module'''
import asyncio
import random


async def wait_random(max_delay=10):
    '''random delay'''
    ran_value = random.uniform(0, max_delay)
    return await asyncio.sleep(ran_value, result=ran_value)
