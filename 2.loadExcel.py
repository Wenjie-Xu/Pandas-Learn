import pandas as pd

# 通过header指定从第几行读取
people = pd.read_excel('/Users/apple/Desktop/People.xlsx', header=0)

# 给没有列名的表设置列名
people = pd.read_excel('/Users/apple/Desktop/People.xlsx', header=None)
people.columns = ['name', 'age', 'home', 'tel']

# 为了防止自动加上索引，我们在read_excel的时候可以主动设置索引列
people = pd.read_excel('/User/apple/Desktop/People.xlsx', index_col='ID')

# 打印大小
print(people.shape)
# 打印列名
print(people.columns)
# 打印前几行
print(people.head(3))
# 打印后几行
print(people.tail(3))
