class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        col = len(matrix[0])-1
        while(col >= 0 and row< len(matrix)):
            if(matrix[row][col]==target):
                return True
            elif(matrix[row][col]>target):
                col = col -1
            else:
                row = row+1
        return False