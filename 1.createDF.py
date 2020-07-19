import pandas as pd

#创建df对象
df =pd.DataFrame({'name':['wenjie','xintao'],'age':[23,24]})

#设置索引
# df.set_index('name',inplace=True)

#导出excel
# df.to_excel('/Users/apple/Desktop/output.xlsx')
print(df)