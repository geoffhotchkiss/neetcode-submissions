# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        from collections import deque

        values = deque()
        
        if head is None:
            return True

        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        while len(values) > 1:
            left, right = values.popleft(), values.pop()
            if left != right:
                return False
        
        if len(values) == 0 or len(values) == 1:
            return True

        return False