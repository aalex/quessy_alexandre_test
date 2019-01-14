#!/usr/bin/env python
"""
Test cases for versionnumber.
"""

from twisted.trial import unittest
from quessyalexandre import versionnumber

# TODO: we should also add some tests for the functions that this higher-level function uses.


class TestVersionNumber(unittest.TestCase):
    def test_simple_numbers(self):
        self.failUnlessEqual(versionnumber.compare_versions('0.1.0', '0.1.1'), versionnumber.RESULT_GREATER)
        self.failUnlessEqual(versionnumber.compare_versions('0.1.1', '0.2.0'), versionnumber.RESULT_GREATER)
        self.failUnlessEqual(versionnumber.compare_versions('2.0.0', '1.0.0'), versionnumber.RESULT_SMALLER)
        self.failUnlessEqual(versionnumber.compare_versions('1.0.0', '1.0.0'), versionnumber.RESULT_EQUAL)

    def test_labels(self):
        self.failUnlessEqual(versionnumber.compare_versions('1.0.0-alpha', '1.0.0-beta'), versionnumber.RESULT_GREATER)
        self.failUnlessEqual(versionnumber.compare_versions('1.0.0-beta', '1.0.0-alpha'), versionnumber.RESULT_SMALLER)
        self.failUnlessEqual(versionnumber.compare_versions('1.0.0-rc1', '1.0.0-rc2'), versionnumber.RESULT_GREATER)
        self.failUnlessEqual(versionnumber.compare_versions('1.0.0-rc1', '1.0.0-rc1'), versionnumber.RESULT_EQUAL)

