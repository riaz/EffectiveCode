from itertools import accumulate 

def find_pivox_index(nums: list[int]) -> int:
    cSum = list(accumulate(nums))
    n = len(nums)
    for idx in range(n):
        left = 0 if idx == 0 else cSum[idx-1]
        right = 0 if idx == n-1 else cSum[n-1] - cSum[idx]
        if left == right:
            return idx
    return -1