# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #init dummyNode and tail
        dummyNode = ListNode
        tail = dummyNode

        #while list1 and list2 are non-empty
        while list1 and list2:

            #if list1 number is les than list 2 number then "append" that onto the linked list
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next #iterate through the next number
            
            #otherwise it mean that list 2 has a lower number than list 1, so "append" that onto the list
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next #set the tail to the next item no matter what
        
        #if there are values of the list(s) left, set tail.next onto them
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        #return the list
        return dummyNode.next
