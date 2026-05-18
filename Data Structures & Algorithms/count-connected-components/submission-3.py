class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = {}
        for x,y in edges:
            if x in graph:
                graph[x].append(y)
            else:
                graph[x]=[y]
            if y in graph:
                graph[y].append(x)
            else:
                graph[y]=[x]
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
        c=0 
        for node in graph.keys():
            if node not in visited:
                dfs(node)
                c+=1
       
        return c + n-len(graph)

              

    