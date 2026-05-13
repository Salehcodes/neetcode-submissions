class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxland = 0
        m,n = len(grid) , len(grid[0])
        visited = set()

        def dfs(x,y):
            if x < 0 or x > m-1 or y < 0 or y > n-1 or (x,y) in visited or grid[x][y]==0:
                return 0
            
            visited.add((x,y))
            return 1+dfs(x-1,y)+dfs(x+1,y)+dfs(x,y-1)+dfs(x,y+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] not in visited and grid[i][j]==1:
                    res = dfs(i,j)
                    maxland = max(maxland,res)
        return maxland