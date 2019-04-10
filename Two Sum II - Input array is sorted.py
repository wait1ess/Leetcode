class Solution:
    def twoSum(self, numbers, target):
        L=len(numbers)
        if L<2 :return []
        left=0
        right=L-1
        while left!=right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            elif numbers[left]+numbers[right]>target:
                right-=1
        return []

if __name__=="__main__":
    numbers=[2,7,11,15]
    target = 9
    answer=Solution().twoSum(numbers,target)
    print(answer)            
