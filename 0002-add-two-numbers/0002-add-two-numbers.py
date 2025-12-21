# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        carry=0
        p1,p2=l1,l2
        while p1 or p2 or carry:

            x=p1.val if p1 else 0
            y=p2.val if p2 else 0
            total=x+y+carry
            digit=total%10
            carry=total//10
            tail.next = ListNode(digit)
            tail = tail.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummy.next
        





