# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
            if not preorder or not inorder:
                return None
                
            self.pre_idx = 0
            
            return self.buildTreeHelper(preorder, inorder, 0, len(inorder) - 1)

        def buildTreeHelper(self, preorder: List[int], inorder:List[int], left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            root = preorder[self.pre_idx]

            self.pre_idx += 1

            location = inorder.index(root)
            
            return TreeNode(root , self.buildTreeHelper( preorder , inorder, left , location - 1 ) , self.buildTreeHelper( preorder , inorder, location + 1 , right)) 

            
            

