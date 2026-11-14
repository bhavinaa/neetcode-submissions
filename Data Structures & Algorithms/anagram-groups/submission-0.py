class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result  = {}
        for i in range(0,len(strs)):
            temp = [0] * 26
            for j in range(0,len(strs[i])):
                c = strs[i][j]
                v = ord(c) - ord('a')
                t = temp[v]
                temp[v] = t + 1
            if tuple(temp) not in result.keys():
                result[tuple(temp)] = [strs[i]]
            else:
                v2 = result[tuple(temp)]
                result[tuple(temp)].append(strs[i])
                
        return list(result.values())


                        

            
        