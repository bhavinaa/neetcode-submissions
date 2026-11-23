class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # number + index
        all = {}
        for i in range(0, len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff in all:
                return [all[diff], i]
            else:
                all[curr] = i
        return [-1,-1] 