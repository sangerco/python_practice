def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    #use slice [::-1] method

    reverse_str = phrase[::-1]

    return reverse_str