#!/usr/bin/env python
"""
Version number comparisons tools.

We follow the semver.org standard.
"""

RESULT_EQUAL = 0
RESULT_GREATER = 1
RESULT_SMALLER = -1


class VersionNumber(object):
    """
    Represents a version number.
    """
    def __init__(self, major, minor=0, patch=0, label=''):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.label = label


def split_version(version_str):
    """
    Major.minor.patch
    """
    major = 0
    minor = 0
    patch = 0
    label = ''
    tokens = []

    tokens = version_str.split('.')
    if len(tokens) > 0:
        major = int(tokens[0])
    if len(tokens) > 1:
        minor = int(tokens[1])
    if len(tokens) > 2:
        try:
            patch = int(tokens[2])
        except ValueError:
            last_token = tokens[2]
            if '-' in last_token:
                subtokens = last_token.split('-')
                patch = int(subtokens[0])
                label = '-'.join(subtokens[1:])

    ret = VersionNumber(major, minor, patch, label)
    return ret


def compare_numbers(int1, int2):
    """
    Compares numbers.
    1 = greater
    0 = equal
    -1 = smaller
    """
    ret = RESULT_EQUAL
    if int2 > int1:
        ret = RESULT_GREATER
    elif int2 < int1:
        ret = RESULT_SMALLER
    else:
        ret = RESULT_EQUAL
    return ret


def compare_labels(label1, label2):
    """
    Compares two labels.
    Examples or labels: '-rc1', '-alpha', '-beta', etc.
    @rtype C{int}
    """
    # TODO: we should check for rcN, where N can be any number
    # FIXME: if there is no label, it should probably be greater than if there is one
    if label1 == label2:
        return RESULT_EQUAL

    LABEL_ORDER = [
        'alpha',
        'beta',
        'gamma',
        'delta',
        'epsilon',
        'rc1',
        'rc2',
        'rc3',
        'rc4',
    ]

    try:
        index_of_label1 = LABEL_ORDER.index(label1)
        index_of_label2 = LABEL_ORDER.index(label2)
        return compare_numbers(index_of_label1, index_of_label2)
    except ValueError: # some element is not in the list
        # Do alphabetical comparison
        first = sorted(label1, label2)
        if first == label2:
            return RESULT_SMALLER
        elif first == label1:
            return RESULT_GREATER


def _compare_version_objects(version1, version2):
    """
    Compares two version number objects.
    @rtype C{int}
    """
    compare_major = compare_numbers(version1.major, version2.major)
    if compare_major != 0:
        return compare_major
    else:
        compare_minor = compare_numbers(version1.minor, version2.minor)
        if compare_minor != 0:
            return compare_minor
        else:
            compare_patch = compare_numbers(version1.patch, version2.patch)
            if compare_patch != 0:
                return compare_patch
            else:
                compare_label = compare_labels(version1.label, version2.label)
                return compare_label


def compare_versions(version1_str, version2_str):
    """
    Compares two version number strings.
    @rtype C{int}
    """
    # TODO: compare build versions as well (+<number>)
    version1 = split_version(version1_str)
    version2 = split_version(version2_str)
    return _compare_version_objects(version1, version2)

