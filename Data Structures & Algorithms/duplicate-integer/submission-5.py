class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(0, len(nums)):
            y = nums[i]
            if y in seen:
                return True
            else:
                seen.add(y)
        return False