class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        present = set()
        for i in range(0,len(nums)):
            item = nums[i]
            if item in present:
                return True
            else:
                present.add(item)
        return False

        