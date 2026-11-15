# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        def dfs(node: TreeNode, sum: int) -> bool:

            if node is None:
                return False
            
            sum += node.val

            if node.left is None and node.right is None:
                if sum == targetSum:
                    return True
                else:
                    sum -= node.val
                    return False
            
            if dfs(node.left, sum):
                return True

            if dfs(node.right, sum):
                return True

            return False
            
        return dfs(root, 0)
            
            

    