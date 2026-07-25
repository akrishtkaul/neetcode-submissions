# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        highest = float('inf')
        lowest = float('-inf')

        return self.helperIsValidBST(root, highest, lowest) 

    def helperIsValidBST(self, root: Optional[TreeNode], h: int, l: int) -> bool:
        if root is None:
            return True

        if root.val >= h or root.val <= l:
            return False
        
        return self.helperIsValidBST(root.left, root.val, l) and self.helperIsValidBST(root.right, h, root.val)

        