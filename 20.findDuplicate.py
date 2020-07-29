import pandas as pd

students = pd.read_excel('/Users/Apple/Desktop/pandas/dumplicate.xlsx')

'生成删除重复后的DataFrame'
# subset:按照哪个删重 / inplace:直接替换 / keep:保留前面的还是后面的
students.drop_duplicates(subset='Name', inplace=True, keep='last')

'找出重复的数据'
# 生成一个数组
dup = students.duplicated()
dup = dup[dup] # 找出重复的Series
print(students.iloc[dup.index]) # 通过索引来定位数据