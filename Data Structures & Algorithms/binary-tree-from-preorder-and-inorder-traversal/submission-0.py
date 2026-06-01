# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        pos = inorder.index(root.val)

        lTree = inorder[:pos]
        rTree = inorder[pos+1:]
        root.left = self.buildTree(preorder[1:pos + 1], lTree)
        root.right = self.buildTree(preorder[pos+1 :], rTree)

        return root