# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        newhead = head
        prev = None
        curr = head

        while curr:
            if curr == newhead and curr.val == val:
                print(f"Dealing with head")
                newhead = curr.next
                prev = None
                curr = newhead
            elif curr.val == val:
                prev.next = curr.next
                if curr.next:
                    print("Removing something in the middle")
                    curr = curr.next
                else:
                    print("Removing a tail")
                    curr = None
            else:
                print("Didn't find it")
                prev = curr
                curr = curr.next

        return newhead

        