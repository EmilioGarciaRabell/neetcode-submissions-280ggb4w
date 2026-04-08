class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            
            for c in string:
                encoded += c
            encoded += "€"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        
        current_string = ""
        for c in s:
        
            if c == "€":
                decoded.append(current_string)
                current_string = ""
            else:
                current_string += c
        return decoded

