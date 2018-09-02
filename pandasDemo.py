

'''
pandas 主要用于数据探索和数据分析
    Series代表了某一串数据
            [index] 索引
    DataFrame数据框

'''
import pandas as pda
#     Series代表了某一串数据
#             [index] 索引
a= pda.Series([8,4,1,2,3])
b=pda.Series([1,2,4,3,6],index=[1,2,3,4,5])
print(a)
print(b)

# 创建数据框
c=pda.DataFrame([[1,23,15],[5,9,5],[45,56,55,5]],columns=['one','two','three','four'])
print(c)

dir=pda.DataFrame({
    "first":1,
    "second":[6,2,3],
    "third":list(str(123)),
     "fourth":[4,5,8]
})
print(dir)

# 取头部数据，默认前五行
print(dir.head(2))
# 取尾部数据，默认后两行
print(dir.tail(2))
#对数据框的数据的数据内容 std标准差  25%分位数
print(dir.describe())
# 转置
print(c.T)






