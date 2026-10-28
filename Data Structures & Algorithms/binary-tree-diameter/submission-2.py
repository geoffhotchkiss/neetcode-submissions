# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Diameter is the length of the longest path between any two nodes. 
Length is the number of edges. 

For every node, calculcate the "height" of the left side and right side. 
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = 0
        right = 0

        def height(n) -> int:
            if n is None:
                return 0
            
            lheight = 0
            rheight = 0

            if n.left:
                lheight = 1 + height(n.left)
            
            if n.right:
                rheight = 1 + height(n.right)

            return max(lheight, rheight)

        max_diameter = 0
        process = [root]

        while len(process) > 0:
            node = process.pop()

            l, r = 0, 0

            if node.left:
                l = 1 + height(node.left)

            if node.right:
                r = 1 + height(node.right)

            max_diameter = max(l+r, max_diameter)

            if node.left:
                process.append(node.left)
            
            if node.right:
                process.append(node.right)

        return max_diameter



