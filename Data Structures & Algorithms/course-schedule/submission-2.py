class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for x, y in prerequisites:
            graph[y].append(x)

        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False

            if node in visited:
                return True

            path.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            path.remove(node)
            visited.add(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True