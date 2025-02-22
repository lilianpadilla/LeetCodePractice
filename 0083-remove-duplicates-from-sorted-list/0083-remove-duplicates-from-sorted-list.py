# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rover = head

        while rover and rover.next:
            if rover.val == rover.next.val:
                rover.next = rover.next.next
            else:
                rover = rover.next
        return head

        