from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        we can reverse scan the digits in the list and insert the carry if it overflows and return digits
        """
        n = len(digits)
        carry = 1
        
        for idx in range(n-1,-1,-1):      
            tmp = digits[idx] + carry      
            digits[idx], carry = tmp % 10, tmp // 10
        if carry:
            digits.insert(0, carry)
        return digits