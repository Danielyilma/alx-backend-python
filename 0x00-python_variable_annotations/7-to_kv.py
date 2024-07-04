#!/usr/bin/python3
'''implement to_kv function'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns string and square if a number as tuple'''
    return (k, v ** 2)
