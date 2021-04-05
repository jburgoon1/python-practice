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
    number_sum = 0
    if start >0:
        number = nums[start:]
        for num in number:
            number_sum += num
    elif not end== None :
        number_end = nums[:end+1:]
        for num_end in number_end:
            number_sum += num_end
    else:
        for numbers in nums:
            number_sum+=numbers
    return number_sum