class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        window = {}
        
        have = 0
        
        for i in t:
            tMap[i] = tMap.get(i,0) + 1
        need = len(tMap)
        res = [-1, -1]
        resLen = float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in tMap and window[c] == tMap[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1

                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l: r + 1] if resLen != float("infinity") else ""

        