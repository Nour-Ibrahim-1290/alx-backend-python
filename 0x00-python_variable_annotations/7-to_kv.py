#!/usr/bin/env python3
""" Defined List datType speciified variable
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return a Tuple of string and unioned list of ints and floats
    """
    return k, float(v ** 2)
