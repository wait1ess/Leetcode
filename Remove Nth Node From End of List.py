# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        L=0
        p1=head
        while p1!=None:
            L+=1
            p1=p1.next
        if L<n or (L==1 and n==1):
            return None
        if L==n:
            return head.next
        p2=head
        k=0
        while p2!=None:
            k+=1
            if k==L-n: break
            p2=p2.next
        p2.next=p2.next.next
        return head


