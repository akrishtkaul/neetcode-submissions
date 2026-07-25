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

        while sumOne and sumTwo:
            number = sumOne.val + sumTwo.val + carry

            if number >= 10:
                carry = (number // 10) % 10
                number %= 10
            else:
                carry = 0
            buildNode.next = ListNode(number)

            sumOne = sumOne.next
            sumTwo = sumTwo.next  
            buildNode = buildNode.next

        while sumOne:
            number = sumOne.val + carry

            if number >= 10:
                carry = (number // 10) % 10
                number %= 10
            else:
                carry = 0
            buildNode.next = ListNode(number)

            sumOne = sumOne.next
            buildNode = buildNode.next


        while sumTwo:
            number = sumTwo.val + carry

            if number >= 10:
                carry = (number // 10) % 10
                number %= 10
            else:
                carry = 0
            buildNode.next = ListNode(number)

            sumTwo = sumTwo.next
            buildNode = buildNode.next

        if carry > 0:
            buildNode.next = ListNode(carry)
        
        return dummyNode.next

            


