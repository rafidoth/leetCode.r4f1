class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r_l = len(grid)
        c_l = len(grid[0])
        
        r = 0
        c = len(grid[0])-1
        count = 0
        while(r<len(grid) and c>=0):
            if(grid[r][c]<0):
                count+= (r_l-r)
                c-=1
            else:
                r+=1
        return count