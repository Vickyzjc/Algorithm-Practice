# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	result = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        # corner case
        if root is None:
        	return result
        
        def helper(treeNode):
            if treeNode is None:
                return
            result.append(treeNode.val)
            helper(treeNode.left)
            helper(treeNode.right)
            
        helper(root)
        return result