
class Solution():
    def longestPalindrome(self, s):
        if not s:
            return ""
        lens=len(s)
        if lens<2:
            return s
        maxlen=0                               # 初始化 最长回文长度
        start=0                                # 初始化 回文起始位置
        dp=[[0]*lens for row in range(lens) ]  # dp数组 维护字串状态

        #step 1  初始化dp数组,完成长度小于3的子串状态判断
        
        for i in range(lens):          # i 为字符索引
            dp[i][i]=1
            if i<lens-1 and s[i]==s[i+1]:
                print (i,":",s[i]," ",i+1,':' ,s[i+1] )
                dp[i][i+1]=1
                start=i
                maxlen=2                           

        #step 2  i为子串长度，j为子串起始地址，r为子串结束地址
        #        逐步得到长度为i的子串状态，利用状态转移方程完成这一判断
        
        for i in range(3,lens+1):                # 遍历子串长度为3以上的子串 
            for j in range(0,lens-i+1):          # 子串起始索引
                r=j+i-1                          # 根据长度i得到终止索引
                if dp[j+1][r-1] and s[j]==s[r]:  # 状态转移方程
                    dp[j][r]=1
                    maxlen=i                     # 更新回文长度
                    start=j

        #step 3 根据第二步得到的最长子串长度和起始位置，得到最终结果
        if maxlen>=2:
            return s[start:start+maxlen]
        return s[0]

if __name__ == "__main__":
    s="abcda"
    answer=Solution().longestPalindrome(s)
    print(answer)

