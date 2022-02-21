class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # corner case
        if (matrix is None) or (len(matrix) == 0) or (matrix[0] is None) or (len(matrix[0]) == 0):
        	return False

        rows = len(matrix)
        cols = len(matrix[0])

        i = 0
        j = cols - 1

        while (i >= 0 and i < rows and j >= 0 and j < cols):
        	if matrix[i][j] == target:
        		return True
        	elif matrix[i][j] < target:
        		i = i + 1
        	else:
        		j = j - 1

        return False
