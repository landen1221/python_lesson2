def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    return create_dict(num1) == create_dict(num2)



def create_dict(nums):
    nums = str(nums)
    return {i: nums.count(i) for i in nums}




