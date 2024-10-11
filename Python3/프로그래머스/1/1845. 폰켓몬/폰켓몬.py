def solution(nums):
    n= len(nums)
    unique_cnt = len(set(nums))
    if unique_cnt>n/2:
        return n/2
    return unique_cnt