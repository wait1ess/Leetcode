class Solution:
    def convert(self,s, numRows):
        PositonArray=[[0]*len(s)  for i in range(numRows)]
        i=0
        j=0
        if numRows==1:return s
        NonZigZag=2*numRows-2
        DownSideNum=NonZigZag/2
        ReadbyLine=""
        for element in s:
            PositonArray[i][j]=element
            if 0<=j%NonZigZag<=DownSideNum-1:
                i=i+1
            else:
                i=i-1
            j=j+1
        for i in range(numRows):
            j=i
            while j<len(s):
                ReadbyLine+=PositonArray[i][j]
                if 0<=j%NonZigZag<=DownSideNum-1:
                    j=j+NonZigZag-2*i
                else:
                    j=j+2*i
        return ReadbyLine


if __name__=="__main__":
    s="dijkstra"
    answer=Solution().convert(s,4)
    print(answer)
    ans=["" for i in range(5)]
    print(ans)


'''
    for index,element in enumerate(s):
        print(index,element)
        if (index+1)%numRows==1:
            PositonArray[0][index]=1
            
        elif (index+1)%numRows==2:
            PositonArray[1][index]=1
            
        else:
            PositonArray[2][index]=1'''
