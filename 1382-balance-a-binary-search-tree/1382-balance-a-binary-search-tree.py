# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_nodes = []

        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            sorted_nodes.append(node)
            inorder_traversal(node.right)
        
        inorder_traversal(root)

        def build_balanced_bst(start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            root_node = sorted_nodes[mid]

            root_node.left = build_balanced_bst(start, mid - 1)
            root_node.right = build_balanced_bst(mid + 1, end)

            return root_node

        return build_balanced_bst(0, len(sorted_nodes) - 1)
            