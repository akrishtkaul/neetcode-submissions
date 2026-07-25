# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sumOne, sumTwo = l1, l2
        exponent = 0
        carry = 0
        dummyNode = ListNode(0)
        buildNode = dummyNode

        while sumOne or sumTwo or carry:
            val1 = sumOne.val if sumOne else 0
            val2 = sumTwo.val if sumTwo else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            buildNode.next = ListNode(digit)
            buildNode = buildNode.next

            sumOne = sumOne.next if sumOne else None
            sumTwo = sumTwo.next if sumTwo else None

        return dummyNode.next
            


