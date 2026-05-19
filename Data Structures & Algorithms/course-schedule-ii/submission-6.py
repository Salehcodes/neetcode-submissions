class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses) }

        for x,y in prerequisites:
            graph[x].append(y)
        visited=set()
        output=[]

        def dfs(node,path):
            if node in path:
                return False
            if node in visited:
                return True
            path.append(node)
            for nei in graph[node]:
                if not dfs(nei,path):
                    return False
            visited.add(node)
            output.append(node)
            path.remove(node)
            return True


        for i in range(numCourses):
            path=[]
            if not dfs(i,path):
                return []

        return (output)