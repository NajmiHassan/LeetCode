# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node):
            return node and not node.left and not node.right

        def dfs(node, is_left):
            if not node:
                return 0
            if is_leaf(node) and is_left:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)
