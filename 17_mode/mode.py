def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    used = []
    most_common = 0
    highest_count = 0

    for i in nums:
        if i not in used:
            x = nums.count(i)
            used.append(i)
            if x > highest_count:
                highest_count = x
                most_common = i

    return most_common
