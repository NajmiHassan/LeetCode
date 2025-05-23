# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal moves
            if not node:
                return 0
            
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)

            moves += abs(left_excess) + abs(right_excess)

            return node.val - 1 + left_excess + right_excess

        moves = 0
        dfs(root)
        return moves
