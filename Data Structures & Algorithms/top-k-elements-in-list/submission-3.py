class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_v = {}
        for num in nums:
            k_v[num] = 1 + k_v.get(num, 0)
        result = []
        for num, count in k_v.items():
            result.append([count, num])

        #sorted(result, key = lambda kv: kv[0])
        result.sort()
        
        ans = []
        count = 0
        while len(ans) < k:
            ans.append(result.pop()[1])
        return ans 



        