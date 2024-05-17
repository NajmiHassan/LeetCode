# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        
        return root

    def printTree(root:TreeNode, depth=0, label="Root:"):
        indent = " " * (4 * ddepth)
        if root is not None:
            print(f"{indent}{label} {root.val}")
            printTree(root.left, depth + 1, "L---")
            printTree(root.right, depth + 1, "R---")
        else:
            print(f"{indent}{label} None")
    
