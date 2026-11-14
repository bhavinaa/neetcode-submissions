class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k_v_store = {}
        for i in range(0, len(nums)):
            temp = nums[i]
            if temp in k_v_store:
                return True
            k_v_store[temp] = 1

        return False         