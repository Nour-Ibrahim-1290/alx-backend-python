#!/usr/bin/env python3
""" Annotate parameters
"""


from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Augment the following code with the correct duck-typed annotations
    """
    if lst:
        return lst[0]
    else:
        return None
