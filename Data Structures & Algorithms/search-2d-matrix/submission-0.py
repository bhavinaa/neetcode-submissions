class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # no of rows
        rows = len(matrix)
        # no of columns 
        columns = len(matrix[0])
        
        r = 0
        c = columns - 1
        while r < rows and c >=0:
            # you assume you found that row
            if matrix[r][c] > target:
                c = c - 1
            elif matrix[r][c] < target:
                r = r + 1
            else:
                return True
        return False