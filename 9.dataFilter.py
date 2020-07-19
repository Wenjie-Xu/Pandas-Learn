import pandas as pd

'python中独特的写法,返回布尔值'


def age_18_to_30(x):
    return 18 <= x < 30


def level_a(x):
    return x > 85


students = pd.read_excel('/Users/apple/Desktop/Student.xlsx', index_col='name')

# 在python中使用loc，相当于SQL中的where
# 中括号中的返回boolean，返回True的行将会被保留，最终还是DataFrame
students = students.loc[students['age'].apply(age_18_to_30)]
# students = students.loc[students['score'].apply(level_a)]

'高级语法的写法'
# 换行的字符是（ \）:空格+反斜线
students = students.loc[students.score.apply(lambda x: x > 85)]

print(students)
