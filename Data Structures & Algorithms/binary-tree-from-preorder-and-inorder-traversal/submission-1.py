# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderIdx = {}
        for idx, num in enumerate(inorder):
            inOrderIdx[num] = idx

        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None

            node = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            pos = inOrderIdx[node.val]

            node.left = dfs(l, pos - 1)
            node.right = dfs(pos + 1, r)
            return node
        
        return dfs(0, len(inorder) - 1)