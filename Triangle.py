# 将一个二维数组排列成金字塔的形状，找到一条从塔顶到塔底的路径，使路径上的
# 所有点的和最小，从上一层到下一层只能挑相邻的两个点中的一个。
# 把triangle二维数组转化：
# 把每一行的数列都左对齐
# 上一行到下一行就两个选择，横坐标不变或加一
class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)

        dp = triangle[-1] # 创建与金字塔底层同样长度的dp数组，记录状态，初始化为底层元素
                          # dp[i]表示从底层到这一层的第i个元素所有路径中最小的和

        for i in range(n-2,-1,-1):  # 从倒数第二行开始
            for j in range(i+1):    # 每行的每个元素计算最优值
                # 递推关系：
                # 下一行与它相邻的两个节点中比较小的再加上它自己的值
                # 从倒数第二层开始网上，变化数字，dp[-1]一开始就用不到了
                dp[j] = min( dp[j], dp[j+1] ) + triangle[i][j]
                print(dp)
        return dp[0]
if __name__=="__main__":
    triangle=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    answer=Solution().minimumTotal(triangle)
    print(answer)
