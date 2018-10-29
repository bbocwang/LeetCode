class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row==0 and col==0:
                    result[0][0]=grid[0][0]
                elif row == 0 and col != 0:
                    print([row,col])
                    result[row][col]=result[row][col-1]+grid[row][col]
                elif row !=0 and col == 0:
                    result[row][col]=result[row-1][col]+grid[row][col]
                else:
                    result[row][col]=min(result[row-1][col],result[row][col-1])+grid[row][col]
        return result[len(grid)-1][len(grid[0])-1]

a=Solution()
test=[[1,3,1],[1,5,1]]
print(a.minPathSum(test))
