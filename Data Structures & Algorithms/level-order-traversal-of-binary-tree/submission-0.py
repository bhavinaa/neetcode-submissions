# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        lst = []
        lst.append(root)
        result = []

        while lst:
            temp = []
            for _ in range(0, len(lst)):
                re = lst.pop(0)
                left = re.left
                right = re.right
                if left != None:
                    lst.append(left)
                if right != None:
                    lst.append(right)
                temp.append(re.val)
            result.append(temp)
        return result

            
                