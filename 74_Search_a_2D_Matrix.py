class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        temp = 0
        for i in range(m):
            if target <= matrix[i][-1]:
                temp = i
                break
        
        for i in range(n):
            if target == matrix[temp][i]:
                return True

        return False

        