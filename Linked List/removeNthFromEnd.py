# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #initialize a dummy node and left and right points at dummy and head respectively
        dummy = ListNode(0, head)
        l, r = dummy, head

        #this while loop functions to shift the right pointer by n
        while n > 0 and r:
            r = r.next
            n -= 1
        
        #this simply increments l and r until right pointer reaches null
        while r:
            l = l.next
            r = r.next

        #by re-assigning connection, the link to the nth node is already lost so it is deleted
        l.next = l.next.next

        #return the new linked list 
        return dummy.next
        
        
