def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # create new list

    new_lst = []

    # loop through given list and add true elements into new list

    for el in lst:
        if el:
            new_lst.append(el)

    return new_lst

    # could also do a comprehension

    # return [el for el in lst if lst]