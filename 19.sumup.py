import pandas as pd

students = pd.read_excel('/Users/Apple/Desktop/pandas/sumuo.xlsx')

# 多列series的提取方法,将数字列进行提取
temp = students[['chinese', 'english', 'math']]
# 给定参数，按行统计
result1 = temp.sum(axis=1)  # 求和
result2 = temp.mean(axis=1)  # 求平均
students['sum'] = result1
students['average'] = result2

# 对现有列按列求和
temp2 = students[['chinese', 'english', 'math', 'sum', 'average']].sum()
temp2['stu_name'] = 'Summary'
# 将结果插入DataFrame中
students = students.append(temp2, ignore_index=True)
print(students)
