class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_counter = Counter(words)
        word_len = len(words[0])
        total_words = len(words)
        window_len = total_words * word_len
        result = []

        for i in range(word_len):
            left = i
            seen = defaultdict(int)
            count = 0
            
            for right in range(i,len(s)-word_len + 1 , word_len):
                word = s[right:right+word_len]
                
                if word in word_counter:
                    seen[word] +=1
                    count+=1

                    while seen[word] > word_counter[word]:
                        left_word = s[left:left+word_len]
                        seen[left_word] -=1
                        left +=word_len
                        count-=1

                    if count == total_words:
                        result.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return result