# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def getIntersectionNode(self, headA, headB):
        if headA==None or headB==None: return None
        p1=headA
        p2=headB
        cycle=1
        while p1!=p2 and cycle<=2:
            p1=p1.next
            p2=p2.next
            if p1==None:
                p1=headB
                cycle+=0.5
            if p2==None:
                p2=headA
                cycle+=0.5
        if p1==p2 :
            return p1
        return None
