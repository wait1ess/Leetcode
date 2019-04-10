# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if head==None : return None
        if head.next==None :return head
        P1=head
        head=head.next
        P1.next=head.next
        head.next=P1
        while P1!=None and P1.next!=None and P1.next.next!=None:
            P2=P1.next
            P3=P2.next
            P1.next=P3
            P2.next=P3.next
            P3.next=P2
            P1=P2
        return head
