#!/usr/bin/python3
"""method determines if given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Number of bytes to expect for each character"""

    expected_bytes = 0

    for num in data:

        if num >> 7 == 0:
            if expected_bytes > 0:
                return False
        else:
            mask = 0b10000000
            while (num & mask) == mask:
                expected_bytes += 1
                mask >>= 1

            if expected_bytes == 1 or expected_bytes > 4:
                return False

        expected_bytes = max(expected_bytes - 1, 0)

    return expected_bytes == 0
