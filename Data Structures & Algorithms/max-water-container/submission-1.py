class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # you have to look at the length
        i = 0
        j = len(heights) - 1
        total = (j-i) * min(heights[j], heights[i])
        i = 1
        while i < j:
            width = j - i
            height = min(heights[j], heights[i])
            temp = width * height
            if heights[j] < heights[i]:
                j = j - 1
            else: 
                i = i + 1
            total = max(total, temp)
        return total 


        