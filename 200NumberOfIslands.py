class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:return 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        def dfs(grid,x,y,m,n):
            if x<0 or y<0 or x>=m or y>=n or grid[x][y]=='0':
                return
            grid[x][y]='0'
            dfs(grid,x-1,y,m,n)
            dfs(grid,x+1,y,m,n)
            dfs(grid,x,y-1,m,n)
            dfs(grid,x,y+1,m,n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid,i,j,m,n)
        return res
