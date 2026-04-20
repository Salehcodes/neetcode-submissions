class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n= len(board) , len(board[0])
        visited = set()

        def dfs(i,j,index):
            if index == len(word):
                return True
            
            if (i < 0 or i >= m or j < 0 or j >= n) or (i,j) in visited or (word[index] != board[i][j]) :
                return False
            visited.add((i,j))
            res =  dfs(i+1,j,index+1) or dfs(i-1,j,index+1) or dfs(i,j+1,index+1) or dfs(i,j-1,index+1)
            visited.remove((i,j))
            return res
        
        for x in range(m):
            for y in range(n):
                if dfs(x,y,0):
                    return True
        
        return False

        

            