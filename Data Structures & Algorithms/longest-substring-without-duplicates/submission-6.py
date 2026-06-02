class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
      
        
        word_set = set()
        
        window = 0
        for r in range(len(s)):
            while s[r] in word_set:
                word_set.remove(s[l])
                l += 1
            word_set.add(s[r])
            window = max(window,r - l + 1)

        return window