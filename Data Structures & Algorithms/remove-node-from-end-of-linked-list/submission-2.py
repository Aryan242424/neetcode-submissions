# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        target_index = length - n
        curr, prev = head, None

        count = 0
        while curr and count < target_index:
            count += 1
            prev, curr = curr, curr.next
        
        # target reached
        if count == 0: return head.next
        prev.next = curr.next
        
        return head
        