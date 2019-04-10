#列举出所有合法的括号匹配，使用dfs。
#如果左括号的数量大于右括号的数量的话，就不能产生合法的括号匹配。
class Solution:
    def helpler(self, l, r, item, res):       # l,r为还需要填入的左右括号数
        if r < l:                             # 判断为非法
            return
        if l == 0 and r == 0:                 # 符合 加入
            res.append(item)
        if l > 0:                             # 左递归
            self.helpler(l - 1, r, item + '(', res)
        if r > 0:                             # 右递归
            self.helpler(l, r - 1, item + ')', res)
    
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res

if __name__=="__main__":
    N=2
    answer=Solution().generateParenthesis(N)
    print(answer)
