from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        We can use a map as a index to append the values, and flatten the dict to get the values
        """
        res = []
        mapping = defaultdict(list)

        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            for j in range(m):
                index = i + j
                if index % 2 == 0:
                    mapping[index].insert(0, mat[i][j])
                else:
                    mapping[index].append(mat[i][j])
        for _,v in mapping.items():
            res.extend(v)
        return res
        
