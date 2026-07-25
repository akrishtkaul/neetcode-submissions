# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        leftHeight = self.isBalancedHelper(root.left)
        rightHeight = self.isBalancedHelper(root.right)

        return (
            abs(leftHeight - rightHeight) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )


    
    def isBalancedHelper(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0

        return 1 + max(self.isBalancedHelper(root.left), self.isBalancedHelper(root.right))


        