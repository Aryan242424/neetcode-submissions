# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        curr = head

        while True:
            end = self.get_kth(curr, k -1)
            if not end: break # no more

            next_group = end.next

            self.reverse_list(curr, next_group)

            group_prev.next = end
            curr.next = next_group

            group_prev = curr
            curr = next_group

        return dummy.next

    def reverse_list(self, start, end):
        prev = end
        curr = start
        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return start
    
    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        





        

