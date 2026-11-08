# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []

        que = deque()
        que.append(root)
        result = []

        while que:
            items = []
            for i in range(len(que)):
                item = que.popleft()
                items.append(item.val)
                if item.left:
                    que.append(item.left)
                if item.right:
                    que.append(item.right)
            
            result.append(items)
        
        return result
                










      





        