# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n = 0 
        m = 0
        exponent = 0

        sumOne = l1
        sumTwo = l2

        while sumOne and sumTwo:
            n = n + (sumOne.val * (10 ** exponent))
            m = m + (sumTwo.val * (10 ** exponent))
            sumOne = sumOne.next
            sumTwo = sumTwo.next
            exponent += 1

        if sumOne:
            while sumOne:
                n = n + (sumOne.val * (10 ** exponent))
                sumOne = sumOne.next
                exponent += 1

        if sumTwo:
            while sumTwo:
                m = m + (sumTwo.val * (10 ** exponent))
                sumTwo = sumTwo.next
                exponent += 1
        
        finalSum = n + m

        dummyNode = ListNode(0)
        buildNode = dummyNode

        if finalSum == 0:
            return ListNode(0)

        while finalSum:
            buildNode.next = ListNode( finalSum % 10 )
            finalSum //= 10
            buildNode = buildNode.next

        buildNode.next = None
        
        return dummyNode.next

            


