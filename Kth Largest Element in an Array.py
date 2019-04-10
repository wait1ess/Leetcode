class Solution:       
    def findKthLargest(self, nums, k):
        L=len(nums)
        if k>L :return None
        if L==1: return nums[0]
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
        quick_sort(nums,start,end)
        print(nums)
        return nums[L-k]

if __name__=="__main__":
    nums=[1,3,7,90,1,3,5,6,8,0]
    k = 4
    answer=Solution().findKthLargest(nums,k)
    print(answer)
    

        
