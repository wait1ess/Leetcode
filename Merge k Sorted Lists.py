# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        L=len(lists)
        if L==0 :return None
        if L==1 :return lists[0]
        l = []
        for lst in lists:              # 链表转数组
            while lst:
                l.append(lst.val)
                lst = lst.next

        def quick_sort(S,start,end):   # (子)数组的快速排序，start为在原数组上的开始索引
            if start>=end: return
            pivot=S[end]               # 轴
            left=start                 # 左游标
            right=end-1                # 右游标
            while left<=right:
                while left<=right and S[left]<=pivot: left+=1
                
                while left<=right and S[right]>pivot: right-=1
                if left<=right:
                    S[left],S[right]=S[right],S[left]
                    left+=1
                    right-=1
            S[left],S[end]=S[end],S[left]      # 将轴放于“中间”，左小右大
            quick_sort(S,start,left-1)
            quick_sort(S,left+1,end)    
        start=0
        end=L-1
        quick_sort(l,start,end)
        
        def list_to_linknode(array):   # 数组转链表
            head=ListNode(None)
            temp=head
            for element in array:
                temp.next=ListNode(element)
                temp=temp.next
            return head.next
        return list_to_linknode(l)











        
