# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr, l2_curr = l1, l2
        carry = 0
        dummy = ListNode(0)
        l3_curr = dummy

        while l1_curr or l2_curr:
            val1 = l1_curr.val if l1_curr else 0
            val2 = l2_curr.val if l2_curr else 0
            new_val = val1 + val2 + carry
            if new_val < 10: 
                carry = 0
            else:
                carry = 1
                new_val -= 10
            
            l3_curr.next = ListNode(new_val)
            l3_curr = l3_curr.next
            l1_curr, l2_curr = l1_curr.next if l1_curr else None, l2_curr.next if l2_curr else None
        
        if carry == 1:
            l3_curr.next = ListNode(1)
        

        return dummy.next
            
            
            