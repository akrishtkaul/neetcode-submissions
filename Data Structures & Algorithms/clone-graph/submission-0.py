"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        hm = {}
        listofNodes = deque()
        listofNodes.append(node)
        hm[node] = Node(node.val)

        while len(listofNodes) > 0:

            currentNode = listofNodes.popleft()

            for neighbor in currentNode.neighbors:
                if neighbor not in hm.keys():
                    listofNodes.append(neighbor)
                    hm[neighbor] = Node(neighbor.val)
            
                hm[currentNode].neighbors.append(hm[neighbor])
        
        return hm[node]

            
        