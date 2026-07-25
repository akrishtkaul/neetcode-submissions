# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        dq = deque()
        nodes = []

        dq.append(root)

        while len(dq) > 0:
            
            level_size = len(dq)
            level = []
         
            for _ in range(level_size):

                currentNode = dq.popleft()
                level.append(currentNode.val)

                if currentNode.left is not None:
                    dq.append(currentNode.left)
                
                if currentNode.right is not None:
                    dq.append(currentNode.right)
                    
            nodes.append(level)
                


        
        return nodes


        
        



    
        