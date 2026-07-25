# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        dummyOne = head 
        median = head

        while dummyOne and dummyOne.next:
            median = median.next
            dummyOne = dummyOne.next.next

        prev = None
        curr = median.next 
        median.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr 
            curr = nxt

        left = head
        right = prev

        while right:
            leftNext = left.next
            rightNext = right.next
            left.next = right
            right.next = leftNext
            left = leftNext
            right = rightNext
        
        

        