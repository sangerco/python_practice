def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """

    # create new list

    new_nums = []

    # create product variable

    product = 1

    # push evens into new list

    for num in nums:
        if num % 2 == 0:
            new_nums.append(num)

    # check list length for edge case, then loop through to multiply nums

    if len(new_nums) == 0:
        return product
    else:
        for num in new_nums:
            product = num * product
        return product