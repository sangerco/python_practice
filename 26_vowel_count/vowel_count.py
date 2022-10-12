def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    # lower case phrase

    new_phrase = phrase.lower()

    # create dictionary comprehension

    vowels = {char: new_phrase.count(char) for char in 'aeiou'}

    # create new dictionary to move non-zero characters in

    new_vowels = {}

    for (key, value) in vowels.items():
        if value > 0:
            new_vowels[key] = value

    return new_vowels