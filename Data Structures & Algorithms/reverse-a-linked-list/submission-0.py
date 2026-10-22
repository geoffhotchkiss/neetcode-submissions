# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
We're trying to reverse the arrows 
A B C D
0 1 2 3

A.val  = 0
A.next = B
B.val  = 1
B.next = C
C.val  = 2
C.next = D
D.val  = 3
D.next = None
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None


        # Reverse head
        """
            0 -> 1 -> 2 -> 3 
         <- 0    1    2    3  
            L    R 
        """
        L = head
        R = L.next
        L.next = None
        
        while R is not None:
            """
            <- 0    1 -> 2 -> 3  
              tmp   L    R 
            """
            tmp = L
            L = R
            R = L.next
            L.next = tmp

        return L
        
