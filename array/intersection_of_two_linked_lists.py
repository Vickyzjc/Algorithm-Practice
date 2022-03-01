# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA is None) or (headB is None):
        	return None

        pointA = headA
        pointB = headB

        while pointA != pointB:
        	if pointA is None:
                pointA = headB
            else:
                pointA = pointA.next
        	
            if pointB is None:
                pointB = headA
            else:
                pointB = pointB.next

        return pointA