#!/usr/bin/python3
'''implementing element_length function'''
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''iterating an iterator'''
    return [(i, len(i)) for i in lst]
