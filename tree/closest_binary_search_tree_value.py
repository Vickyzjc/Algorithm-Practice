# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        cur = root
        record = root

        while cur is not None:
        	if abs(cur.val - target) < abs(record.val - target):
        		record = cur

        	if cur.val < target:
        		cur = cur.right
        	else:
        		cur = cur.left

        return record.val