# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def recurv(root: Optional[TreeNode]) -> int:
            if root == None or self.balanced == False:
                return 0
            hL = recurv(root.left)
            hR = recurv(root.right)

            if abs(hL - hR) > 1:
                self.balanced = False
            return max(hL, hR) + 1

        recurv(root)
        return self.balanced