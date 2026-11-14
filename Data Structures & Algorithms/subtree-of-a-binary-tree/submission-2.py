# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isEqual(self, a, b):
        if a == None and b == None:
            return True
        if a == None or b == None:
            return False
        if a.val == b.val:
            return self.isEqual(a.right, b.right) and self.isEqual(a.left, b.left)
        else:
            return False
                
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        
        if subRoot == None:
            return True
        if root == None:
            return False

        if self.isEqual(root, subRoot):
            return True
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)