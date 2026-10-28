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
        
        max_diameter = 0

        def height(n) -> int:
            nonlocal max_diameter
            if n is None:
                return 0
            
            lheight = height(n.left)
            rheight = height(n.right)

            max_diameter = max(max_diameter, lheight + rheight)
            
            return 1 + max(lheight, rheight)

        height(root)

        return max_diameter



