# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1==None:return l2
        if l2==None:return l1
        p1=l1
        p2=l2
        p3=ListNode(None)
        l3=p3
        while p1!=None and p2!=None:
            if p1.val<=p2.val:
                p3.next=p1
                p3=p3.next
                p1=p1.next
            elif p1.val>p2.val:
                p3.next=p2
                p3=p3.next
                p2=p2.next
        p3.next=p2 or p1

        return l3.next
        
