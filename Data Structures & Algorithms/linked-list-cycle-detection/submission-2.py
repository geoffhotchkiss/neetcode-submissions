# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Let's try fast/slow pointers here. 

slow advences one at a time
fast does two, if they are equal there's a cycle 

"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while True:
            if slow is None or fast is None:
                return False

            slow = slow.next

            fast = fast.next
            # advance two, check that we don't overrun
            if fast is None:
                return False
            else:
                fast = fast.next

            if slow == fast:
                return True