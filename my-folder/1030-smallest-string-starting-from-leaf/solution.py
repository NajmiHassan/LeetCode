# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            if not node:
                return
            path.append(chr(node.val + ord('a')))
            if not node.left and not node.right:
                nonlocal result
                current_string = ''.join(reversed(path))
                if not result or current_string < result:
                    result = current_string
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        result = ''
        dfs(root, [])
        return result
