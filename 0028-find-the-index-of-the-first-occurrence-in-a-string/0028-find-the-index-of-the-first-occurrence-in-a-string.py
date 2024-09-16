class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        right = len(needle)
        left = 0
        if needle == haystack:
            return 0
        
        while left<right:
            if right > len(haystack):
                return -1
            if haystack[left:right] == needle:
                return left
            else:
                left+=1
                right+=1
        return len(haystack) -1
