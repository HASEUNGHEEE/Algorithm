def solution(nums):
    return min(len(nums)/2, len(set(nums)))
    
    '''
    unique_nums = len(set(nums))
    if len(nums) / 2 > unique_nums:
        return unique_nums
    else:
        return len(nums) / 2
    '''