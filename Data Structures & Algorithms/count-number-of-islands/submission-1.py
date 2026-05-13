class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        islands=0
        def dfs(x,y):
            if x < 0 or x>m-1 or y < 0 or y > n-1 or (x,y) in visited or grid[x][y]=="0":
                return

            visited.add((x,y))
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)




        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands+=1
                    visited.add((i,j))
        return islands
