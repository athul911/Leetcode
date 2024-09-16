class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        i,j = 0,0
        max_len = 0

        while(i<len(s)):
            if s[i] in chars:
                chars.remove(s[j])
                j+=1
                continue
            chars.append(s[i])
            i+=1
            max_len = max(max_len,len(chars))
        
        return max_len