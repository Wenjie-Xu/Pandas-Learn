import pandas as pd

pd.options.display.max_columns = 999 # 设置展现的最大列数

students = pd.read_excel('/Users/Apple/Desktop/pandas/transpose.xlsx', index_col='name')

table = students.transpose() # 旋转数据后生成新的DataFrame
print(table)