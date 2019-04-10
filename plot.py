import matplotlib.pyplot as plt
import itertools
import warnings
import xlrd



# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd


#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的位置  ，by_index：表的索引
def excel_table_byindex(file= 'table_tp.xlsx',colnameindex=0,by_index=0):
    data = xlrd.open_workbook('table_tp.xlsx')
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) # 列名
    List =[]
    List.append(colnames)
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             List.append(row)
    return List



table6 = excel_table_byindex(by_index=0)
table7 = excel_table_byindex(by_index=1)
table8 = excel_table_byindex(by_index=2)
table9 = excel_table_byindex(by_index=3)
   

'''
def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=12)
    ax.set_ylabel('y-label', fontsize=12)
    ax.set_title('Title', fontsize=14)

fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)

for ax in axs.flatten():
    example_plot(ax)

plt.show()
'''
