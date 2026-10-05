# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, l:Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, l

        while curr:
            nxt = curr.next
            curr.next = prev #reversing a pointer

            prev = curr
            curr = nxt
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rl1 = self.reverseList(l1)
        rl2 = self.reverseList(l2)
        carry = 0
        dummy = ListNode()
        curr = dummy
        while rl1 or rl2 or carry:
            val1 = rl1.val if rl1 else 0
            val2 = rl2.val if rl2 else 0
            result = val1 + val2 + carry

            carry = result // 10
            result = result % 10
            curr.next = ListNode(result)
            curr = curr.next
            rl1 = rl1.next if rl1 else None
            rl2 = rl2.next if rl2 else None

        return self.reverseList(dummy.next)




    
