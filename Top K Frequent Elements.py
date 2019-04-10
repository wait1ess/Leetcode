'''

class Solution:
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        print (count.get)
        return heapq.nlargest(k, count.keys(), key=count.get) 
'''
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        d={}
        for element in nums:
            if element not in d:
                d[element]=1
            else:
                d[element]+=1
        print(d)
        heap=[]
        for key, value in d.items():
            heapq.heappush(heap,(value, key))    #heap  ()
        print(heap)
        sorted_nums = []
        while heap:
            sorted_nums.append(heapq.heappop(heap))
        print(sorted_nums)
        TopK=[]

        for i in range(k):
            TopK.append(sorted_nums.pop()[1])
            i+=1
        return TopK

if __name__=="__main__":
    nums =[-1,-1]
    k = 1
    answer=Solution().topKFrequent(nums, k)
    print(answer)
