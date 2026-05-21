# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(branch: Optional[TreeNode], subBranch: Optional[TreeNode]):
            if branch == None and subBranch == None:
                return True
            if branch == None or subBranch == None or branch.val != subBranch.val:
                return False
            return sameTree(branch.left, subBranch.left) and sameTree(branch.right, subBranch.right)

        if root == None:
            return False
        if (sameTree(root, subRoot)):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
         
                        