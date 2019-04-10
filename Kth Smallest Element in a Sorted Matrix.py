class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)                            # 行数
        L, R = matrix[0][0], matrix[n-1][n-1]      # 左右游标 初始化
        while L < R:                               # 
            mid = L + ((R-L) //2)                  # “中位点”
            temp = self.search_lower_than_mid(matrix, n, mid)  # 返回“中位点”是矩阵中第temp小的数
                                                                # 然后k比较，进行二分查找
            if temp < k:                                        # LR的“中位点”不够大，更新L
                L = mid + 1
            else:                                               # 更新R
                R = mid                                        
        return L                                   # left和right最终会相等，并且会变成数组中第k小的数字

    def search_lower_than_mid(self, matrix, n, x):  
                                                    
        i = 0                                       # 从第一行的最后一个元素开始                          
        j = n - 1                                   
        cnt = 0                                      
        while i < n and j >= 0:                     
            if matrix[i][j] <= x:                  # 如果目标数在比该行的尾元素大，则cnt累加该行元素的个数，遍历下一行
                i += 1
                cnt += j + 1
            else:                                  # 直至到达该行某列元素比目标数大
                j -= 1
        return cnt                                 # 遍历完所有的行可以找出中间数是第几小的数


if __name__=="__main__":
    matrix = [[1,2],[3,3]]
    k = 2
    answer=Solution().kthSmallest(matrix, k)
    print(answer)
