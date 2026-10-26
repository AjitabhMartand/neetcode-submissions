# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left),height(node.right))
        if root is None:
            return 0
        left_Height = height(root.left)
        right_Height = height(root.right)
        curr_D = left_Height+right_Height
        left_Diameter = self.diameterOfBinaryTree(root.left)
        right_Diameter = self.diameterOfBinaryTree(root.right)
        return max(curr_D,left_Diameter,right_Diameter)