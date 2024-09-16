class Solution:
    def intToRoman(self, num: int) -> str:
        res=""
        nums = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,"V": 5, "IV": 4, "I": 1}
        
        roman_map = OrderedDict(nums)


        for key,value in roman_map.items():
            count = num//value
            if count:
                res+= count * key
                num = num%value
        return res