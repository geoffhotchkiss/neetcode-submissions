# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        
        process = [p, q]

        while len(process) > 0:
            t1 = process.pop()
            t2 = process.pop()

            if t1 is None and t2 is None:
                continue

            if t1.val != t2.val:
                return False
   
            # If they both have a left, check them
            # If one side's left is None while the other isn't, not the same!
            if t1.left is not None and t2.left is not None:
                process += [t1.left, t2.left]
            elif (t1.left is None and t2.left is not None) or (t1.left is not None and t2.left is None):
                return False
            
            # Same except for right
            if t1.right is not None and t2.right is not None:
                process += [t1.right, t2.right]
            elif (t1.right is None and t2.right is not None) or (t1.right is not None and t2.right is None):
                return False

            # I think this condition doesn't matter... 
            if t1.left is None and t1.right is None and t2.left is None and t2.right is None:
                continue

        return True



        