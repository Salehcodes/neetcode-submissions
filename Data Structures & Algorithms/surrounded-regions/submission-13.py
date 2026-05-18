class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m,n = len(board) , len(board[0])
        visited=set()
        drcs = [[1,0],[-1,0],[0,1],[0,-1]]

        def IsOnBorder(x,y):
            return board[x][y] == "O" and (x==0 or x==m-1 or y==0 or y==n-1)
            
        def isValid(x,y):
            return x >=0 and x<m and y>=0 and y<n



        def dfs(x,y,indexes):
                 

            res = True
            visited.add((x,y))
            indexes.append((x,y))
            if IsOnBorder(x,y):
                res= False
            for drc in drcs:
                new_x,new_y=x+drc[0],y+drc[1]
                if isValid(new_x,new_y) and (new_x,new_y) not in visited and board[new_x][new_y]=="O": 
                    if not dfs(new_x,new_y,indexes):
                        res = False
            return res
        
        
        for x in range(m):
            for y in range(n):
                if board[x][y]=="O" and (x,y) not in visited:
                    indexes=[]
                    if dfs(x,y,indexes):
                        for (i,j) in indexes:
                            board[i][j]="X"


