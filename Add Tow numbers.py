# Definition for singly-linked list.

'''Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.'''    
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def list_to_linknode(array):
        head=ListNode(None)
        temp=head
        for element in array:
            temp.next=ListNode(element)
            temp=temp.next
        return head.next


    def addTwoNumbers(self, l1, l2):
        L1=[]
        L2=[]
        L3=[]
        while l1:
            L1.append(l1.val)
            l1=l1.next
        while l2:
            L2.append(l2.val)
            l2=l2.next
        print(L1,L2)
        num1=0
        num2=0
        for index,element in enumerate(L1):
            num1+=element*(10**index)
            print(num1)
        for index,element in enumerate(L2):
            num2+=element*(10**index)
            print(num2)
        sum=num1+num2
        if sum==0:
            L3.append(0)
        else:
            while sum != 0:
                L3.append(sum % 10)
                sum//= 10
                print(L3)
        l3=list_to_linknode(L3)
        return l3

        
if __name__=='__main__':
    def list_to_linknode(array):
        head=ListNode(None)
        temp=head
        for element in array:
            temp.next=ListNode(element)
            temp=temp.next
        return head.next
    l1=list_to_linknode([0])
    l2=list_to_linknode([0])
    answer=Solution().addTwoNumbers(l1,l2)
    print(answer.val)
