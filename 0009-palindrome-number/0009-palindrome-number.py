class Solution:
    def isPalindrome(self, x: int) -> bool:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        if x < 0:
            return False
        digits = 0
        y = x
        while(x):
            remainder = x%10
            digits = digits * 10 + remainder
            x= x//10
        
        if digits > MAX_INT or digits < MIN_INT:
            return False
        if digits == y :
            return True
