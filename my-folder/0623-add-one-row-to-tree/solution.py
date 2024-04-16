# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
    
        queue = [(root, 1)]
    
        while queue:
            node, cur_depth = queue.pop(0)
        
            if cur_depth == depth - 1:
                # Insert val as left child of node
                new_left = TreeNode(val)
                new_left.left = node.left
                node.left = new_left
                
                # Insert val as right child of node
                new_right = TreeNode(val)
                new_right.right = node.right
                node.right = new_right
            else:
                if node.left:
                    queue.append((node.left, cur_depth + 1))
                if node.right:
                    queue.append((node.right, cur_depth + 1))
                
        return root
