class Solution:       
    def findKthLargest(self, nums, k):
        arr=nums[0:k]
        self.heap_MinTop(arr)
        for element in nums[k:]:
            if element >arr[0]:
                arr[0]=element
                self.sink(arr,0,k)
        return arr[0]

    
    def sink(self,arr,i,n):                      # 小元素节点下沉 堆顶元素索引为1
        while 2*i+1<=n-1:
            j=2*i+1
            if j+1<=n-1 and arr[j]>arr[j+1]:
                j+=1
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
            i=j

    def heap_MinTop(self,arr):
        n=len(arr)
        for i  in range(n//2,-1,-1):
            self.sink(arr,i,n)


if __name__=="__main__":
    nums=[3,2,1,5,6,4]
    k = 2
    answer=Solution().findKthLargest(nums, k)
    print(answer)
    
