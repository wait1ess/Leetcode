class Solution(object):
    def isAnagram(self, s, t):
        ls=len(s)
        lt=len(t)
        if ls!=lt:return False
        ds={}
        dt={}
        for element in s:
            if element not in ds:
                ds[element]=1
            else:
                ds[element]+=1
        for element in t:
            if element not in dt:
                dt[element]=1
            else:
                dt[element]+=1
        for key in ds:
            if key not in dt or dt[key]!=ds[key]:
                return False
        return True


if __name__=="__main__":
    s = "anagram"
    t = "nagarbm"
    answer=Solution().isAnagram(s, t)
    print(answer)
