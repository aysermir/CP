# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        def find1Leaves(root):
            if root == None:
                return
            if root.left == None and root.right == None:
                l1.append(root.val)
            left = find1Leaves(root.left)
            right = find1Leaves(root.right)
            return
        find1Leaves(root1)
        def find2Leaves(root):
            if root == None:
                return            
            if root.left == None and root.right == None:
                l2.append(root.val)
            left = find2Leaves(root.left)
            right = find2Leaves(root.right)
            return
        find2Leaves(root2)
        if l1 == l2:
            return True
        return False    
