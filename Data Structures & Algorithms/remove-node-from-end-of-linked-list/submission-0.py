# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        lead = dummy
        prevBoi = dummy
        counter = 0

        while lead:
            lead = lead.next
            counter += 1

            if counter > n :
                break
        
        while lead:
            lead = lead.next
            prevBoi = prevBoi.next

        if not prevBoi:
            prevBoi.next = None
        elif not prevBoi.next:
            prevBoi.next = None
        else:
            prevBoi.next = prevBoi.next.next

        return dummy.next


        
        