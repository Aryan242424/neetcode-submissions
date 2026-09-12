# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # node positions not the 
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = self.reverse_linked_list(slow.next)
        slow.next = None
        left = head
        
        # left is always >= right
        while right:
            left_temp, right_temp = left.next, right.next
            right.next = left_temp
            left.next = right

            left = left_temp
            right = right_temp
    


    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
        
