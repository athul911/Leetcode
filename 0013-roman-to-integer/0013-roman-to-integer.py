class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        nums = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

        for i in range(len(s)):
            if i+1 < len(s) and nums[s[i]] < nums[s[i+1]]:
                res-=nums[s[i]]
            else:
                res+=nums[s[i]]

        return res