#!/usr/bin/python3
"""
Module to validate whether a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): A list of integers representing the data set.
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        num_bytes -= 1
    return num_bytes == 0


if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))

    data2 = [80, 121, 116, 104, 111, 110, 32, 105,
             115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))
