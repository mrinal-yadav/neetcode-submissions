class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        row = 0
        while t <= b:
            mid_row = (t + b)//2
            if target > matrix[mid_row][-1]:
                t = mid_row + 1
            elif target < matrix[mid_row][0]:
                b = mid_row - 1
            else:
                break
        
        if not (t <= b):
            return False
        row = (t + b) // 2
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False