import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('/Users/Apple/Desktop/pandas/join.xlsx',
                         sheet_name='stu', dtype={'stu_id': str})
scores = pd.read_excel('/Users/Apple/Desktop/pandas/join.xlsx',
                       sheet_name='score', dtype={'stu_id': str})

# merge的时候如果左右表的字段名不一致，则使用left_on和right_on，两边一致使用on即可
# join相当于简化版的merge，只能通过index做inner join

table = students.merge(scores, how='left', on='stu_id').fillna(0)
table.score = table.score.astype(int) # 将浮点型转为int
print(table)
