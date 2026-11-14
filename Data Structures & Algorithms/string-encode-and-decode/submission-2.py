class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(0,len(strs)):
            result = result + "#c" + str(len(strs[i])) + "#" + strs[i]
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        # starting pointer of the list
        i = 0
        while i < len(s):
            j = 0
            while s[i:i+2] == "#c":
                j = i + 2
                length = 0 
                string_ref = ""
                while s[j] != "#":
                    string_ref += s[j]
                    j = j + 1
                length = int(string_ref)
                word = s[j + 1:  j+ length + 1]
                result.append(word)
                
                i = j + length
                break
            i = i + 1
        return result

            
