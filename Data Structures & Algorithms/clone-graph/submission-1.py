"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        q = deque()
        q.append(node)
        dct = {}
        cloned = Node(node.val)
        dct[node]=cloned
        while q:
            curr = q.popleft()
            cloned = dct[curr]

            for ni in curr.neighbors:
                if ni not in dct:
                    q.append(ni)
                    nicopy = Node(ni.val)
                    dct[ni] = nicopy
                cloned.neighbors.append(dct[ni])

        return dct[node]
        


            