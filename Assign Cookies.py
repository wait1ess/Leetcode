class Solution:
    def quick_sort(self,S,start,end):   # (子)数组的快速排序，start为在原数组上的开始索引
        if start>=end: return
        pivot=S[end]               # 轴
        left=start                 # 左游标
        right=end-1                # 右游标
        while left<=right:
            while left<=right and S[left]<=pivot: left+=1
            while left<=right and S[right]>pivot: right-=1
            if left<=right:
                S[left],S[right]=S[right],S[left]
                left+=1
                right-=1
        S[left],S[end]=S[end],S[left]      # 将轴放于“中间”，左小右大
        self.quick_sort(S,start,left-1)
        self.quick_sort(S,left+1,end)    
        
    def findContentChildren(self, g, s):
        self.quick_sort(g,0,len(g)-1)
        self.quick_sort(s,0,len(s)-1)

        g_length = len(g)
        s_length = len(s)
        

        if (g_length == 0 or s_length == 0):
            return 0
        
        i = s_length - 1
        j = g_length - 1
        satisfied_children = 0
        while ( i >= 0 and j >= 0 ):
            if s[i] >= g[j]:
                satisfied_children += 1
                i -= 1
                j -= 1
            elif s[i] < g[j]:
                j -= 1
                
        return satisfied_children


if __name__=="__main__":
    g=[3,4,5,1,6,8,9,0,1,1,10]
    s=[1,3,7,90,1,3,5,6,8,0]
    answer=Solution().findContentChildren( g, s)
    print(answer)
    print(g,s)
