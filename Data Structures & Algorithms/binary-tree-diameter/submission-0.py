# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            if root == None:
                return -1
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                re = 2 + left + right
                result[0] = max(result[0], re)

                return 1 + max(left , right)
        dfs(root)
        return result[0]
        