# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #init previous and current pointers respectively
        prev, curr = None, head

        #while current exists
        while curr:

            #set a temp reference to the next element and switch the pointers accordingly
            temp = curr.next
            curr.next = prev
            prev = curr

            #set the curr pointer to the temp reference
            curr = temp
        
        return prev
