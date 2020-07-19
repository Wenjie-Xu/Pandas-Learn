import pandas as pd

'创建Series(序列) Index-Value'
# 方法1：列表的形式(Index - Value)
ser_a = pd.Series([1, 2, 3], index=['a', 'b', 'c'], name='sea')
# 方法2：字典的形式(Index - Value)
ser_b = pd.Series({'a': 4, 'b': 5, 'c': 6}, name='seb')

'创建DataFrame(数据框架) 二维Index'
# 方法一：将Series作为行创建(列表形式)
df_a = pd.DataFrame([ser_a, ser_b])
print(df_a.index)
# 方法二：将Series作为列创建(字典形式)
df_b = pd.DataFrame({ser_a.name: ser_a, ser_b.name: ser_b})
print(df_b.index)

# 以行的形式创建，默认：索引将作为列名，name作为索引，没有name，将自动生成
# 以列的形式，必须以字典形式，所以一定会存在一个列名
# 以列的形式创建，索引作为索引，name作为列名