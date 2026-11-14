class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total = defaultdict(list) # key [letter count] : list of words

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            total[tuple(count)].append(s)
        
        return list(total.values())