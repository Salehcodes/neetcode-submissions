class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid) , len(grid[0])
        visited = set()
        q = deque()
        
        def addnei(x,y):
            if  x < 0 or x > m-1 or y > n-1 or y < 0 or grid[x][y]==-1 or (x,y) in visited:
                return
            q.append([x,y])
            visited.add((x,y))
        
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))
        distance = 0 
        while q:
            for i in range(len(q)):
                [x,y] = q.popleft()
                grid[x][y] = distance
                addnei(x+1,y)
                addnei(x-1,y)
                addnei(x,y-1)
                addnei(x,y+1)
            distance+=1

