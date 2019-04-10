
class Solution:
     
    def reverse(self, x):
        temp=[]
        if -2147483648<=x<0:
            i=-1
        elif x==0 or x<-2147483648 or x>2147483647:
            return 0
        else:
            i=1
        x=i*x
        remainter=0
        answer=0
        l=len(str(x))-1
        print(l)
        while x!=0:
            remainter=x%10
            print(remainter)
            answer=answer+remainter*10**l
            x=x//10
            l=l-1
        if i*answer<-2147483648 or i*answer>2147483647:
            return 0
        return i*answer
            

if __name__=="__main__":
    x=1534
    answer=Solution().reverse(x)
    print(answer)
            
            
