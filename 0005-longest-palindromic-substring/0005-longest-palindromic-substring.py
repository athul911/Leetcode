class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        def expand(left,right):
            while left>= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]

        for i in range(len(s)):
            new_str = expand(i,i)
            if len(new_str) > len(longest):
                longest = new_str

            new_str = expand(i,i+1)
            if len(new_str) > len(longest):
                longest = new_str

        return longest