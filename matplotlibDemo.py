'''

    # 折线图/散点图   plot



'''

import matplotlib.pylab as pyl
import numpy as nu

x = [1, 2, 9, 15, 20, 30]
y = [5, 6, 5, 15, 20, 15]
x1 = [5, 6, 5, 15, 20, 15]
y1 = [5, 6, 5, 15, 20, 15]

'''
# plot(x,y,数据图样式) 默认折线图 ‘o’则是散点图
更改颜色
    c 青色
    r hongse
    g 绿色
    b 蓝色
    y 黄色
    k 黑色
    w 白色
    
线条样式
    -直线
    --虚线
    -. -.形式
    :   细小虚线
    
点的样式
    s   方形
    h   六角形
    H   六角形
    *   *形
    +   加号
    x   x型
    d   菱形
    D   菱形
    p   五角形
    
'''
# 表示蓝色图的虚线散点图
pyl.plot(x1, y1)
pyl.plot(x, y, '--sb')
# 设置图的标题
pyl.title("display")
# x轴的内容
pyl.xlabel("x-")
# y轴的内容
pyl.ylabel("y-")
# 更改x的长度范围
pyl.xlim(0,40)
# 更改y的长度范围
pyl.ylim(0,40)
pyl.show()


