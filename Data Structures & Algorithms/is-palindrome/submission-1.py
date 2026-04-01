class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_to_right = ""
        right_to_left = ""
        last_char = len(s) - 1
        for i in range(len(s)):
            if s[i].isalnum():
                left_to_right += s[i].lower()
            
            if s[last_char].isalnum():
                right_to_left += s[last_char].lower()
            last_char -= 1        
        return left_to_right == right_to_left