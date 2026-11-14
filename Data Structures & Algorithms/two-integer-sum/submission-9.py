class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = {}
        for i, n in enumerate(nums):
            # you have the key as the index, so there is no re
            k[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in k and k[diff] !=i:
                return [i, k[diff]]
        return [] 



        