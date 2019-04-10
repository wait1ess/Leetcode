class Solution:
    def maxArea(self, height):
        L=len(height)
        if L <=1: return 0
        left=0
        right=L-1
        Max_Area=(L-1)*min(height[0],height[L-1])
        while right!=left:
            H=min(height[left],height[right])
            area=H*(right-left)
            print(H)
            print(left,right)
            Max_Area=max(area,Max_Area)
            print("max",Max_Area)
            if height[left]<height[right]:left+=1
            elif height[left]>height[right]:right-=1
            elif height[left]==height[right]:
                if height[left+1]>=height[right]:left+=1
                else:right-=1
        return Max_Area

if __name__=="__main__":
    height=[0,0,0,0,1,1]
    answer=Solution().maxArea(height)
    print(answer)
            
