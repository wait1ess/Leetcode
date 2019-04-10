class Solution:
    def maxProduct(self, nums):
        if nums is None: return0
        dp=[[0 for _ in range(2)] for _ in range(2)]

        dp[0][1]=nums[0] # 初始化正max
        dp[0][0]=nums[0] # 初始化负max
        res=nums[0]      # 初始化结果

        for i in range(1,len(nums)):
            x,y=i%2,(i-1)%2              # 前后交替（递推仅需要前一次dp结果）
            dp[x][0]=max(dp[y][0]*nums[i],dp[y][1]*nums[i],nums[i])  # 更新局部最大
            dp[x][1]=min(dp[y][0]*nums[i],dp[y][1]*nums[i],nums[i])  # 更新局部负最大
            res=max(res,dp[x][0])

        return res
