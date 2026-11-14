class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            curr = nums[i]
            old_v = target - curr
            if (old_v in count):
                temp = count[old_v]
                return [temp, i]
            else:
                count[curr] = i
        return [-1,-1]