import pandas as pd
# Series的索引和Dataframe的索引是对齐关系，取并集

s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')

# 如果以列的形式添加到DataFrame中，则需要以Dict形式（指明列名）
df1 = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})

# 如果以行的形式添加到DataFrame，则直接传递series列表
df2 = pd.DataFrame([s1, s2, s3])
print(df2)
