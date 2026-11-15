class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        i = 0
        j = len(numbers) -1 

        while i < j:
            tempSum = numbers[i] + numbers[j]
            if tempSum == target:
                return [i + 1,j + 1]
            if tempSum > target:
                j = j - 1
            if tempSum < target:
                i = i + 1
        return [0,0]