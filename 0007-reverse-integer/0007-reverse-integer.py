class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = -x
        digit = 0
        while(x):
            remainder = x%10
            digit = digit*10 +remainder
            x = x//10
        if negative:
            digit = -digit
        if digit < -2 **31 or digit > 2**31:
            return 0
        return digit

