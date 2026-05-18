class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights) , len(heights[0])

        res = []
        drcs = [[0,1],[0,-1],[1,0],[-1,0]]

        def containstwoseas(indexes):
            pacific = False
            atlantic = False
            for x,y in indexes:
                if x==0 or y==0:
                    pacific = True
                if x==m-1 or y==n-1:
                    atlantic = True
            return pacific and atlantic   


        def dfs(x,y,visited):
            if x<0 or x>=m or y<0 or y>=n or (x,y) in visited:
                return
            visited.add((x,y))
            for drc in drcs:
                new_x,new_y = x+drc[0],y+drc[1]
                if not (new_x<0 or new_x>=m or new_y<0 or new_y>=n or (new_x,new_y) in visited):
                    if heights[new_x][new_y] <= heights[x][y]:
                        dfs(new_x,new_y,visited)

        
        for x in range(m):
            for y in range(n):
                if True:
                    visited = set()
                    dfs(x,y,visited)
                    if containstwoseas(visited):
                        res.append([x,y])
        return res

