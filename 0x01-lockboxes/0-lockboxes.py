#!/usr/bin/python3
"""A python module that determines if all boxes can be opened
   from a list of lists
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    unlocked = [False] * len(boxes)  # Track unlocked status for each box
    unlocked[0] = True  # The first box is unlocked
    keys = set(boxes[0])  # Start with keys from the first box

    # Keep track of boxes we have checked to avoid infinite loops
    checked_boxes = set()

    while keys:
        new_keys = set()
        for key in keys:
            if key < len(boxes) and not unlocked[key]:
                # Unlock the box and mark it as checked
                unlocked[key] = True
                checked_boxes.add(key)
                # Add new keys from the unlocked box
                new_keys.update(boxes[key])
        # Update keys with the new keys found
        keys = new_keys.difference(checked_boxes)

    return all(unlocked)
