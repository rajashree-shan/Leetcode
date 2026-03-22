# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        fast=head
        while fast is not None:
            if fast.val==val:
                slow.next=fast.next
            else:
                slow=slow.next
            fast=fast.next
        return dummy.next
