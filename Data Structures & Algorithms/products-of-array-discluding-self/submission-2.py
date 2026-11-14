class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1 
        isThereZero = False 
        zeros = []
        for i in range(0, len(nums)):
            if nums[i] == 0:
                isThereZero = True
                zeros.append(i)
                total = total * 1
            else:
                total = total * nums[i]
        result = [0] * len(nums)

        if len(zeros) > 1:
            return result
        
        if len(zeros) == 1:
            result[zeros[0]] = total
            return result
        if len(zeros) == 0:
            for i in range(0, len(nums)):
                result[i] = total // (nums[i])
            return result
            