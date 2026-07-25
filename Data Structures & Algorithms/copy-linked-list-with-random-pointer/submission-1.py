"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hm = {}

        p = head

        while p:
            hm[p] = Node(p.val)
            p = p.next

        for old_node, copied_node in hm.items():
            copied_node.next = hm.get(old_node.next)
            copied_node.random = hm.get(old_node.random)
        
        return hm.get(head)


        