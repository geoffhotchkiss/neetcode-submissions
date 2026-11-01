# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head

        curr = head
        right = curr.next
        head.next = None

        while right:
            tmp = right.next # safe because we have a right, but this *could* be None
            right.next = curr 
            curr = right
            right = tmp

        return curr
            
