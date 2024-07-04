#!/usr/bin/env python3
'''implements make_multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''return callable'''
    func: Callable[[float], float] = lambda input: multiplier * input

    return func
