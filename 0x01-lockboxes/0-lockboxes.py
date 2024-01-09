#!/usr/bin/python3
""" Lockboxes"""


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened."""

    if not boxes or len(boxes) == 1:
        return True

    keys = set(boxes[0])
    opened = {0}

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in opened:
            opened.add(key)
            keys.update(boxes[key])

    return len(opened) == len(boxes)
