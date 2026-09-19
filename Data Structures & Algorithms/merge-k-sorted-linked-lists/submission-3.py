# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
                list1, list2 = lists[0], lists[1]
                dummy = ListNode(0)
                curr = dummy
                while list1 and list2:
                    if list1.val < list2.val:
                        # then
                        curr.next = list1
                        list1 = list1.next
                    else:
                        curr.next = list2
                        list2 = list2.next
                    curr = curr.next
                if not list1: curr.next = list2
                else: curr.next = list1
                return dummy.next
        else:
                mid = len(lists) // 2

                left = self.mergeKLists(lists[:mid])
                right = self.mergeKLists(lists[mid:])

                return self.mergeKLists([left, right])

        
        

        