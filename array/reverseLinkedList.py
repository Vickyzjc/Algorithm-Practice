# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1: DFS from up to bottom
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None):
        	return head

        return self.helper(None, head)

    def helper(self, prev, cur):
    	if cur is None:
    		return prev
    	next = cur.next
    	cur.next = prev
    	return self.helper(cur, next)

