class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposites = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        for c in s:
            if c in opposites:
                if stack:
                    currElement = stack.pop()
                    
                else:
                    currElement = "."

                if opposites[c] != currElement:
                    return False
            else:
                stack.append(c)
            
        
        return not stack
            