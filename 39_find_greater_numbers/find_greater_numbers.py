def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        2

        >>> find_greater_numbers([6, 1, 2, 7])
        3

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    count = 0
    cur_index = 1

    for i in nums:
        for j in nums[cur_index:]:
            if j > i:
                count += 1
                break
        cur_index += 1

    return count
