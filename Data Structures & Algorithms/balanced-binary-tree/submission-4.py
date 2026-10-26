# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def height(n):
            l = 0
            r = 0

            if n is None:
                return 0

            if n.left:
                l = 1 + height(n.left)
            
            if n.right:
                r = 1 + height(n.right)

            return max(l, r)

        lh = height(root.left)
        rh = height(root.right)
        lb = self.isBalanced(root.left)
        rb = self.isBalanced(root.right)

        if root.left:
            lh += 1
        
        if root.right:
            rh += 1

        print(f"{lh=} {rh=}")

        return abs(lh - rh) <= 1 and lb and rb