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
            if root == None:
                return 0
            print(root.val)
            hL = recurv(root.left)
            hR = recurv(root.right)

            diff = abs(hL - hR)
            print("Diff between" + str(root.left) + " | " + str(root.right) + " = " + str(diff))
            if diff > 1:
                self.balanced = False
                print(self.balanced)
            return max(hL, hR) + 1

        recurv(root)
        print(self.balanced)
        return self.balanced