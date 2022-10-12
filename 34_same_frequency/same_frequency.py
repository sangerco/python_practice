def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    list_1 = [int(num) for num in str(num1)]
    list_2 = [int(num) for num in str(num2)]

    list_1.sort()
    list_2.sort()

    if list_1 == list_2:
        return True

    return False    