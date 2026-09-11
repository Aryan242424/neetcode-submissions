# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None

        prev = None
        curr = head
        while curr.next:
            next_node = curr.next # store next 
            curr.next = prev #reassign next to prev 
            prev = curr # curr becomes prev for next iteration
            curr = next_node #curr becomes next
        curr.next = prev
    
        return curr
        