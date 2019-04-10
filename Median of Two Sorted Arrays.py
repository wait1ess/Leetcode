class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1,n2  = len(nums1), len(nums2)
        if n1 > n2:
            nums1, nums2, n1, n2 = nums2, nums1, n2, n1                # 交换，让第二个列nums2和n2更大

                                                                       
        imin, imax = 0, n1                                             # 标记数组nums1的起点，终点 
        half_len = (n1 + n2 + 1) // 2                                  # half_len分割，若为奇数，中位数算入half_len即左侧
                                                                       # half_len为两组数组分入左侧的元素的总个数（全程固定）
        
        while imin <= imax:                                            # 二分查找的标准循环条件

            i = (imin + imax) // 2                                     # 二分查找标准迭代条件.i 为nums1分入左侧的个数
                                                                       #                     （i 初始化为len(nums1)//2 ）
            j = half_len - i                                           #                      j 为nums2分入左侧的个数
                                                                       #                      (j 初始化为half_len剩下的那部分 )
                                                                       
            if j > 0 and i < n1 and nums1[i] < nums2[j-1]:             # 情况一： nums1右侧最小值小于nums2左侧最大值
                imin = i + 1                                           # 增加进入num1的元素个数
                
            elif i > 0 and j < n2 and nums1[i-1] > nums2[j]:           # 情况二： nums1左侧最大值大于nums2右侧最小值
                imax = i - 1                                           # 减少进入num1的元素个数
                
            else:                                                      # 情况三：左侧最大小于右侧最小，且元素个数两侧相等
                                                                                 # （得到匹配的i和j）
                if i == 0:                                                       # 所有的nums1大于nums2
                    max_of_left = nums2[j-1]                           
                elif j == 0:                                                     # 所有的nums2大于nums1
                    max_of_left = nums1[i-1]
                else:                                                            # 取左侧最大
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (n1 + n2) % 2 == 1:                                 # 如果总数为奇数 中位数为左侧最大（下面的右侧最小无需计算）
                    return max_of_left

                if i == n1:                                                      # 所有的nums1小于nums2                                                
                    min_of_right = nums2[j]
                elif j == n2:                                                    # 所有的nums1大于nums2 
                    min_of_right = nums1[i]
                else:                                                            # 取右侧最小
                    min_of_right = min(nums1[i], nums2[j])                       

                return (max_of_left + min_of_right) / 2.0                        # 返回左侧最大右侧最小的平均值


if __name__=="__main__":
    nums1=[1,2,5,7]
    nums2=[1,4,7,9,10]
    answer=Solution().findMedianSortedArrays(nums1, nums2)
    print(answer)

































'''
class Solution:
    def findMedianSortedArrays(self, L1, L2 ) :
        class ListNode:
            def __init__(self, x):
                self.val = x
                self.next = None
        def list_to_linknode(array):
            head=ListNode(None)
            temp=head
            for element in array:
                temp.next=ListNode(element)
                temp=temp.next
            return head.next
        def link_median(link):
            i=1
            if (m+n)%2!=0:
                while i !=(m+n+1)/2:
                    link=link.next
                    i=i+1
                return link.val
            else:
                while i !=(m+n)/2:
                    link=link.next
                    i=i+1
                return (link.val+link.next.val)/2
        m=len(L1)
        n=len(L2)
        if L1==[] or (L2!=[] and L1[0]>L2[0]):
            L1,L2=L2,L1
            m,n=n,m
        if L2==[]:
            if m%2==0 and m!=1:
                #print('******')
                return (L1[int(m/2)]+L1[int(m/2-1)])/2
            else:
                #print('#####')
                return L1[int((m-1)/2)]
        
        l1=list_to_linknode(L1)
        l2=list_to_linknode(L2)
        p=ListNode(None)
        p.next=l1
        q=l1
        k=0
        while l2 is not None:          
            if q is not None:
                if l2.val<q.val:      
                    p.next=ListNode(l2.val)
                    p=p.next
                    p.next=q
                    l2=l2.next
                else:
                    p=p.next
                    q=q.next
            else:
                p.next=ListNode(l2.val)
                p=p.next
                l2=l2.next
            k=k+1
            if k>=(m+n+1)/2:
                return link_median(l1)
        link_print(l1)
        return link_median(l1)
        print('%%%%%')

if __name__=="__main__":
    nums1=[2]
    nums2=[1,3,4]
    def link_print(link):
        k=link
        while k is not None:
            print(k.val)
            k=k.next
    
    answer=Solution().findMedianSortedArrays( nums1, nums2 )
    print(answer)
'''
'''
def median(A, B):
    m, n = len(A), len(B)                       #AB长度
    if m > n:                      
        A, B, m, n = B, A, n, m                 #短的为A和m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2 
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0
        '''

    

