# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_balanced(node) -> (int, bool):
            if node is None:
                return (0, True)
            
            left = height_balanced(node.left)
            right = height_balanced(node.right)

            balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1

            height = 1 + max(left[0], right[0])

            return (height, balanced)

        return height_balanced(root)[1]
