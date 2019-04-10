class Solution:
    def longestPalindrome(self, s):
        l=len(s)
        if l==0:return 0
        if l==1:return 1
        d={}
        for element in s:
            if element not in d:
                d[element]=1
            else:
                d[element]+=1
        lenght=0
        for key,value in d.items():
            if value>1 and value%2==0:
                lenght+=value
            elif value>1 and value%2==1:
                lenght+=value-1
        if lenght<l:lenght+=1
        return lenght
if __name__=="__main__":
    s="abccccdd"
    answer=Solution().longestPalindrome(s)
    print(answer)
