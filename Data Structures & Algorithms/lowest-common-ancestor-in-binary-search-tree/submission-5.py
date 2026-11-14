# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # know the property of a BST, that is why what does it mean 
        # and what does it represent is very important to know
        # although you know you want to represent the data in a certain way, you have to know 
        # dont loose focus on what you are trying to find
        # how you are going to change it the other way 

        curr = root
        while curr: 
            
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
                continue
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
                continue
            else:
                return curr
        
       
        