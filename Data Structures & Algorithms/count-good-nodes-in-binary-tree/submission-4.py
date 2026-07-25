# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        goodNodesNumber = []
        self.goodNodesHelper(root, goodNodesNumber, root.val)
        return len(goodNodesNumber)

    def goodNodesHelper(self, root: TreeNode, goodNodesNumber: List[int], max_so_far: int) -> int:
        if root is None:
            return

        if root.val >= max_so_far:
            goodNodesNumber.append(root.val)
            max_so_far = root.val

        self.goodNodesHelper(root.right, goodNodesNumber, max_so_far)

        self.goodNodesHelper(root.left, goodNodesNumber, max_so_far)




        