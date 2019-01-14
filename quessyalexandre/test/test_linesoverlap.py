#!/usr/bin/env python
"""
Test cases for linesoverlap.
"""

from twisted.trial import unittest
from quessyalexandre.linesoverlap import linesoverlap


class TestLinesOverlap(unittest.TestCase):
    def test_simple(self):
        # As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
        self.failUnlessEqual(linesoverlap((1, 5), (2, 6)), True)
        self.failUnlessEqual(linesoverlap((1, 5), (6, 8)), False)
