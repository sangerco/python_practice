def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # convert lists to sets

    set1 = set(l1)
    set2 = set(l2)

    # intersect sets

    set3 = set1 & set2

    # convert new set to list

    new_lst = list(set3)

    return new_lst