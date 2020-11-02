def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    cur_idx = 1
    for i in nums:
        cur_total = i
        if cur_idx + 1 < len(nums):
            for j in nums[cur_idx:cur_idx + 2]:
                cur_total += j

            if cur_total % 2 == 1:
                return True
            cur_idx += 1

    return False


