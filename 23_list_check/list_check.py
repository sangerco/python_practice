def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # loop over list, check type != list if so return false
    # if not return true

    for item in lst:
        if type(item) != list:
            return False

    return True
        