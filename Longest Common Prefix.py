class Solution:
    def longestCommonPrefix(self, strs):
        if strs==[] :return ""
        shortest=min([len(s) for s in strs])
        pre=""
        for i in range(shortest):
            if len(set([s[i] for s in strs] ))==1:
                pre+=strs[0][i]
            else: break
        return pre


if __name__=="__main__":
    s=["flower","flow","flight"]
    answer=Solution().longestCommonPrefix(s)
    print(answer)
