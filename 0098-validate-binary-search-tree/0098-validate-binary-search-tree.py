# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def valid(node,left,right):
            if node is None:
                return True
            if not (left<node.val<right):
                return False
            left_side=valid(node.left,left,node.val)
            if left_side==False:
                return False
            right_side=valid(node.right,node.val,right)
            if right_side==False:
                return False
            return True 

        return valid(root,float("-inf"),float("inf"))