'''
对问题建模： 
整个问题转化为一个图论问题。 
从n到0，每个数字表示一个节点； 
如果两个数字x到y相差一个完全平方数，则连接一条边。 
我们得到了一个无权图。 
原问题转化成，求这个无权图中从n到0的最短路径。 
'''


# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, …）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
class Solution:
    # BFS
    def numSquares(self, n):
        if n < 2:
            return n
        lst = []                      # 候选答案列表
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1

        cnt = 0                       # 初始化最佳步数  
        toCheck = {n}                 # 初始化“当前层”需要被检查的目标值        
        while toCheck:                
            cnt += 1                  # 每“层”搜索增加一次步数
            temp = set()              # 初始化“下一层”的目标值（当前层的所有目标值减去所有可能的候选平方数的可能）
            for x in toCheck:         # 遍历“该层下”的目标值
                for y in lst:         # 候选完美平方数
                    if x == y:        # 最先到达目标值
                        return cnt    # 返回“最短”路径即可
                    if x < y:         # 如果完全平方数大于目标值退出for循环（没必要做无谓计算）
                        break
                    temp.add(x-y)     # 更新“下一层的”的目标值
            toCheck = temp

        #return cnt
