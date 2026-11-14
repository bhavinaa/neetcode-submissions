class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def getOrder(s:str) -> dict:
            freq = {}
            for i in range(0, len(s)):
                if s[i] in freq:
                    freq[s[i]] = freq[s[i]] + 1
                else:
                    freq[s[i]] = 1
            return freq

        return getOrder(s) == getOrder(t)