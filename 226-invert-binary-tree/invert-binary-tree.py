
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        nodes = deque()
        nodes.append(root)

        while nodes:

            temp = nodes.pop()

            if temp.left: 
                nodes.appendleft(temp.left)
            if temp.right:
                nodes.appendleft(temp.right)

            swap = temp.left
            temp.left = temp.right
            temp.right = swap

        return root


        