#!/usr/bin/env python
"""
Line overlapping utilities.
"""

def _is_within(value, range_min, range_max):
    ret = False
    if value >= range_min and value <= range_max:
        ret = True
    return ret


def linesoverlap(line1, line2):
    """
    Checks if two lines on an axis overlap.
    """
    if type(line1) != tuple or len(line1) != 2:
        raise TypeError('arg 1 must be a 2-element tuple')
    if type(line2) != tuple or len(line2) != 2:
        raise TypeError('arg 2 must be a 2-element tuple')

    min1 = min(*line1)
    max1 = max(*line1)
    min2 = min(*line2)
    max2 = max(*line2)

    ret = False
    if _is_within(min1, min2, max2):
        ret = True
    if _is_within(max1, min2, max2):
        ret = True
    if _is_within(min2, min1, max1):
        ret = True
    if _is_within(max2, min1, max1):
        ret = True
    return ret

