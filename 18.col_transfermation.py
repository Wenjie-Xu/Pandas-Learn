import pandas as pd

users = pd.read_excel('/Users/Apple/Desktop/pandas/transfermation.xlsx', dtype={'ID': str})
# Series的str属性，这样字符串可以进行split成DataFrame
# n的意思是切出来所有的保留几个
df = users['Name'].str.split('-', expand=True, n=2)

users['xing'] = df[0].str.upper()
users['ming'] = df[1]
print(users)
