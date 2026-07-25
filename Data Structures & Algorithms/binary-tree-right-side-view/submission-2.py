# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        nodes = []
    
        self.rightSideViewHelper(root, nodes, 0)

        return nodes
    
    def rightSideViewHelper(self, root: Optional[TreeNode], nodes: List[int], levels: int) -> List[int]:
        if root is None:
            return
        
        if levels == len(nodes):
            nodes.append(root.val)
           
        self.rightSideViewHelper(root.right, nodes, levels + 1)
        self.rightSideViewHelper(root.left, nodes, levels + 1)
        
        