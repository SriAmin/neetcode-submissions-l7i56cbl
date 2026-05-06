# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
maxHeight = 0
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0

        def recurv(node) -> int:
            if not node:
                return 0

            leftHeight = recurv(node.left)
            rightHeight = recurv(node.right)
            self.maxDepth = max(self.maxDepth, leftHeight + rightHeight)

            return 1+ max(leftHeight, rightHeight)

        recurv(root)
        return self.maxDepth