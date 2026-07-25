# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        numbers = []
        self.kthSmallestHelper(root, k, numbers)
        print(numbers)
        return numbers[k - 1]
     

    def kthSmallestHelper(self, root: Optional[TreeNode], k:int, numbers:List[int]) -> int:
        if root is None:
            return None
        
        self.kthSmallestHelper(root.left, k, numbers)

        numbers.append(root.val)

        self.kthSmallestHelper(root.right, k, numbers)

    
    



        