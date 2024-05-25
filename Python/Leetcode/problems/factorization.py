"""
Given a number n, find all its factor combinations
"""
import math
from copy import copy
from typing import List

def factorization(n) -> List[List[int]]:
    """
    We need to do DFS + Backtracking to accomplish this
    """
    result = []
    def dfs(res, lst):
        if res == 1: 
            result.append(copy(lst))
        for i in range(2, res+1):
            if res % i == 0:
                lst.append(i)
                dfs(res//i, lst)
                lst.pop()
    dfs(n, [])
    return result 