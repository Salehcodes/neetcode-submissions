class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hasAcycle=False
        connected =False
        graph ={}
        visited=set()
        for x,y in edges:
            if x in graph:
                graph[x].append(y)
            else:
                graph[x]=[y]
            if y in graph:
                graph[y].append(x)
            else:
                graph[y]=[x]
            
        def dfs(node,par):
            nonlocal hasAcycle
            if node in visited:
                hasAcycle = True
                return
            visited.add(node)
            if node in graph:
                for nei in graph[node]:
                    if nei == par:
                        continue
                    dfs(nei,node)
            
        
        dfs(0,-1)
        if len(visited)==n:
            connected=True
        return connected and not hasAcycle
        