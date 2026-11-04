# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        if head is None:
            return False

        fast = fast.next

        """
             v---------^
        1 -> 2 -> 3 -> 4 -> 5 -> 6
        s    f
             s         f
                  s     
        """

        while slow != fast:
            slow = slow.next
            if fast is None:
                return False
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next


        return True