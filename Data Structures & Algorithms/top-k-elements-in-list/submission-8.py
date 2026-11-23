class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(0, len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i],0)
        
        temp = sorted(freq.items(), key=lambda x:x[1], reverse=True)

        result = [item[0] for item in temp]
        return result[0:k]