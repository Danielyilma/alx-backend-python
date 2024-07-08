#!/usr/bin/env python3
'''maesure time of async function'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    '''measures the time it take to run wait_n func'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    return (end_time - start_time) / n
