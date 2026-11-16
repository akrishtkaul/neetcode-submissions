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
        dq.append(root)
        output = []

        while dq:
            n = len(dq)
            level = []
            for i in range(n):
                node = dq.popleft()
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
                level.append(node.val)

            output.append(level)

        return output
        