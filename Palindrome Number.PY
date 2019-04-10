class Solution:
    def isPalindrome(self, x) :
        s=str(x)
        l=len(s)
        if x<0: return False
        if l==0: return False
        if l==1 :return True
        half_len=l//2
        print(half_len)
        print(s[0:half_len][::-1])
        print(s[(l-half_len):])
        if s[0:half_len][::-1]==s[(l-half_len):]:
            return True
        else:return False


if __name__=="__main__":
    x=10
    answer=Solution().isPalindrome(x)
    print(answer)
            
