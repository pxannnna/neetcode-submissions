# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        prev_a = list1
        for _ in range(a-1):
            prev_a = prev_a.next

        after_b = prev_a
        for _ in range(b-a+2):
            after_b = after_b.next


        tail_list2 = list2
        
        prev_a.next = tail_list2
        while tail_list2.next:
            tail_list2 = tail_list2.next
        tail_list2.next = after_b

        return list1



