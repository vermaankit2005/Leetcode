# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        def traverse(node : TreeNode, current_sum: int):

            if not node: 
                return False

            current_sum += node.val

            if not node.left and not node.right:
                if current_sum == targetSum: 
                    return True
                else:
                    current_sum -= node.val
                    return False

            isSolutionOnLeft = traverse(node.left, current_sum)
            isSolutionOnRight = traverse(node.right, current_sum)

            return isSolutionOnLeft or isSolutionOnRight

        return traverse(root , 0)

            
            
        
        
        
        

        

        

            
            
            

            
            
            
            
            

        