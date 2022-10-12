def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """ 

    lst = list(d.keys())

    lst.sort()

    new_lst = []

    new_lst.append(lst[0])
    new_lst.append(lst[len(lst) - 1])

    tup = tuple(new_lst)

    return tup
