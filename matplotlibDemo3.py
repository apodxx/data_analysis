'''
对csv文件进行读取并可视化分析
'''
import  pandas as pad
import numpy as nu
import matplotlib.pylab as mat
data=pad.read_csv('iris.csv')
print(data.shape)
# 查看所有的数
print(data.values)
# 查看第2行(不包含表中的实际第一行)第4列的数
print(data.values[1][3])
# 转置列转成行
dataT=data.T
x=dataT.values[5]
y=dataT.values[4]
mat.plot(x,y)
# mat.hist()
mat.show()
