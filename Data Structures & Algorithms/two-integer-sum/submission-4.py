class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_Map = {}
        for i in range(0,len(nums)):
            v = nums[i]
            diff = target - v
            if diff in prev_Map:
                return [prev_Map[diff], i]
            else:
                prev_Map[v] = i
        return False


        