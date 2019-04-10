'''
Depth-first Search，遍历2d array，
遇到1的时候，就利用dfs把这个岛的区域大小找全。
dps顺序是 左，上，右，下。
在递归dfs之前，要把目前的cell设为0，是为了避免dfs又往回走，每一个数过的cell，就不需要在重复走了。
'''

class Solution():
    def maxAreaOfIsland(self, grid):
        seen = set()                 # 已搜索过的位置
        
        def area(r, c):              # DFS
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])  # 半岛不计入
                    and (r, c) not in seen and grid[r][c]==1):       # 已搜过的，值为0的不计入   
                return 0
            seen.add((r, c))                                      # 该位置添加到已搜索过的位置
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))                  # 继续递归上，下，左，右

        return max(area(r, c)                                     # 遍历每个点，返回最大计数值
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
