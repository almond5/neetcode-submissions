# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Base case: an empty tree is balanced
        if not root:
            return True

        # 1. Compute heights of left and right subtrees
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        # 2. Check current node's balance AND recursively check all descendants
        return (
            abs(left_height - right_height) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def height(self, node: Optional[TreeNode]) -> int:
        # Base case: empty node has height 0
        if not node:
            return 0
        
        # Height is 1 + max height of left or right child
        return 1 + max(self.height(node.left), self.height(node.right))