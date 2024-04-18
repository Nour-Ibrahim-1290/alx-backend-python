#!/usr/bin/env python3
""" Defined List datType speciified variable
"""


from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum of the list of floats and integers
    """
    return float(sum(mxd_lst))
