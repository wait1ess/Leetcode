class Solution:
    def solveNQueens(self, n):
        if n<1: return[]
        self.result=[]
        self.cols,self.pie,self.na=set(),set(),set() # 用三个集合来表示列、正反对角线的占用情况
        self.DFS(n,0,[])
        return self._generate_result(n)

    def DFS(self,n,row,cur_state):      # 一行行的递归
        # recursive termination
        if row >=n:
            self.result.append(cur_state)
            return
        for col in range(n):            # 有冲突
            if col in self.cols or row+col in self.pie or row-col in self.na:
                continue
                                            # 如果没有冲突就把相应的位置置为占用，继续处理下一行
                                            # 相应的位置置为占用，继续处理下一行
            self.cols.add(col)            
            self.pie.add(row+col)
            self.na.add(row-col)

            self.DFS(n,row+1,cur_state+[col])  # 记录当前行的皇后放在了哪一列col

            self.cols.remove(col)              # 进行回溯时要把占用的位置还回去
            self.pie.remove(row+col)
            self.na.remove(row-col)

    def _generate_result(self,n):
        board=[]
        for res in self.result:
            for i in res:
                board.append("."*i+"Q"+"."*(n-i-1))
        return [board[i:i+n] for i in range(0,len(board),n)]
