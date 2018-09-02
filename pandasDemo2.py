'''
数据格式
'''
import pandas as pda

# 对csv文件进行读写
i = pda.read_csv("iris.csv")
# 对csv文件的描述
# print(i.describe())
# 排序
order = i.sort_values(by="other")
# print(order)

# 对excel文件进行操作
# 有错误
# xls = pda.read_csv('example.xls')
# print(xls)

# 对数据库的操作
import pymysql
conn=pymysql.connect(host="127.0.0.1",user="root",password='root',db='think')
sql='select * from think_pandas_data'
# content=pda.read_sql(sql)
# # 有错误
# print(content.describe())

# 对html的操作
# content= pda.read_html("demo.html")
content= pda.read_html("https://book.douban.com")
print(content)

# 导入文本数据
txt=pda.read_table("note")
print(txt)

