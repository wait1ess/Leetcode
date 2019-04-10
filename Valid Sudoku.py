'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''
class Solution():
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowDict = []
        colDict = []
        gridDict = []
        
        for i in range(9):
            rowDict.append([])      # 九行
            colDict.append([])      # 九列
            gridDict.append([])     # 九个九宫格
        
        for i in range(0,9):
            for j in range(0,9):          # 两层嵌套
                curVal = board[i][j]      # 坐标为i+1,j+1的数字

                if curVal == '.':
                    continue              # 为空，则继续
                
                if curVal in rowDict[i]:  # 若已在该行中发现过，返回错误
                    return False
                else:                     # 否则加入行字典
                    rowDict[i].append(curVal)
                
                if curVal in colDict[j]:   # 若已在该列中发现过，返回错误
                    return False
                else:
                    colDict[j].append(curVal) # 否则加入该列字典
                    
            
                grid = (i//3)*3+j//3          # 九宫格对应公式
                if curVal in gridDict[grid]:  # 若已在该九宫格中发现过，返回错误
                    return False
                else:
                    gridDict[grid].append(curVal)   # 否则加入该九宫格字典
        return True
