class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi source bfs
        m,n = len(grid),len((grid[0]))
        minutes=0

        def isvalid(x,y):
            return x >= 0 and x < m and y >=0 and y<n


        q = deque()
        for x in range(m):
            for y in range(n):
                if grid[x][y]==2:
                    q.append([x,y,0])
        
        drcs = [[1,0],[0,1],[-1,0],[0,-1] ]
        while q:
            i,j,minute = q.popleft()
            for drc in drcs:
                new_i = i+drc[0]
                new_j = j+drc[1]
                if isvalid(new_i,new_j) and grid[new_i][new_j]==1:
                    grid[new_i][new_j]=2
                    q.append([new_i,new_j,minute+1])
                    minutes=max(minutes,minute+1)
        for x in range(m):
            for y in range(n):
                if grid[x][y]==1:
                    return -1
        return minutes   

