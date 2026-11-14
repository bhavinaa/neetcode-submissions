class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def word_order(s):
            result = {}
            for i in range(0, len(s)):
                temp = s[i]
                if temp in result:
                    v = result[temp]
                    result[temp] = v + 1
                else:
                    result[temp] = 1
            return result
        
        word_1 = word_order(s)
        word_2 = word_order(t)

        for temp in word_1.keys():
            if temp in word_2:
                v1 = word_1[temp]
                v2 = word_2[temp]
                if v1 != v2:
                    return False
            else:
                return False
        return True
                