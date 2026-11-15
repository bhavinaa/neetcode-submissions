class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
      
    
        while i <= j:
            m = i + ((j - i)//2)
            temp = nums[m]
            if temp < target:
                i = m + 1
            elif temp > target:
                j = m - 1
            else:
                return m
        return -1