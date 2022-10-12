def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    print(phrase)

    # change phrase into a list

    phrase_list = list(phrase)

    swap_upper = to_swap.upper()
    swap_lower = to_swap.lower()

    # create new list to append chars into

    new_phrase_list = []

    for char in phrase_list:
        if char == swap_upper:
           new_phrase_list.append(char.lower())
        elif char == swap_lower:
            new_phrase_list.append(char.upper())
        else:
            new_phrase_list.append(char)

    print(new_phrase_list)

    # change list back to string

    new_phrase = ''.join(new_phrase_list)

    print(new_phrase)

    return new_phrase