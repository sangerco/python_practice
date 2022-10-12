def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    sum = 0

    if start and end:
        print(start, end)
        nums_start_end = nums[start:(end + 1)]
        print(f"start and end {nums}")
        for num in nums_start_end:
            sum = sum + num
        return sum
    
    if start and not end:
        print(start)
        nums_start = nums[start:]
        print(f"start not end {nums}")
        for num in nums_start:
            sum = sum + num
        return sum

    if end and not start:
        if end > len(nums):
            for num in nums:
                sum = sum + num
            return sum
        else:
            print(end)
            nums_end = nums[:(end + 1)]
            print(f"end not start {nums}")
            for num in nums_end:
                sum = sum + num
            return sum

    for num in nums:
        sum = sum + num
    return sum
