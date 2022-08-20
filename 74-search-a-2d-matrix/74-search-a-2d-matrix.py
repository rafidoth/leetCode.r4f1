class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
    

        start = 0
        end = row_len*col_len-1
        while(start<=end):
            mid = (start+end)//2
            r = mid//col_len
            c = mid%col_len
            if(matrix[r][c]==target):
                return True
            elif(matrix[r][c]>target):
                end = mid -1
            else:
                start = mid+1
        return False