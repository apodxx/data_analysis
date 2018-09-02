'''

    # 直方图   hist

'''
import  numpy as nu
import matplotlib.pylab as pyl
# 随机数的生成random_integers(min,max,数量)
# num=nu.random.random_integers(1,20,10)
# print(num)
# # 生成正态分布nomal(avg,西格玛,个数)
# nomal=nu.random.normal(10,0.5,10)
# print(nomal)
# 正态分布生成的直方图
nomal=nu.random.normal(5.0,1.0,10000)

# pyl.hist(nomal)
# pyl.show()
# 随机数生成的直方图
random = nu.random.random_integers(1,20,1000)
# pyl.hist(random)
# 相当于range()函数 在这里相当于给变量random上下限的限制范围
data=nu.arange(2,19,2)
pyl.hist(random,data,histtype='stepfilled')
# pyl.show()
# 绘制子图
# subplot(行，列，当前区域)
pyl.subplot(2,2,1)

# 此间数据在（2,2,1）中显示
pyl.plot([2,3,4],[2,3,4])

pyl.subplot(2,2,2)

# 此间数据在（2,2,2）中显示
pyl.plot([2,3,4],[4,3,2])

pyl.subplot(2,1,2)

# 此间数据在（2,2,2）中显示
pyl.plot([2,3,4],[2,3,4])

pyl.show()



