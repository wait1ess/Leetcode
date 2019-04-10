class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1  or n==0:return 1
        ans=[0]*(n+1)
        print(ans)
        k=0
        for i in range(len(ans)):
            if i==1  or i==0:ans[i]= 1
            else :
                ans[i]=ans[i-1]+ans[i-2]
        print(ans)
        return ans[-1]


if __name__=="__main__":
    n=5
    answer=Solution().climbStairs(n)
    print(answer)
