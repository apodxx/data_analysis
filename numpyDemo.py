import numpy
# 创建一维数组
arr1d = numpy.array([5,2,7,6])
print(arr1d)
# 创建二维数组
arr2d = numpy.array([[6,5,1],[2,4,1],[5,4,9]])
print(arr2d[1][1])
# 排序
arr2d.sort()
arr1d.sort()
print('arr1d排序后的结果:'+str(arr1d))
print("arr2d排序后的记过:"+str(arr2d))
# 取最大值 最小值
y1=arr1d.max()
y2=arr2d.min()
print(y1)
print(y2)
# 切片
print(arr1d[1:3])
print(arr2d[0][1:])
