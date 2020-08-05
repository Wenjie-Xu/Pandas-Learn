import pandas as pd
import numpy as np

pd.options.display.max_columns = 999
orders = pd.read_excel('/Users/Apple/Desktop/pandas/pivot.xlsx')

orders['Year']=pd.DatetimeIndex(orders.Date).year

# 方法一：使用自带的pivot_table函数
pt1 = orders.pivot_table(index='Brand',columns='Year',values='Total',aggfunc=np.sum)

# 方法二：使用group by
groups = orders.groupby(['Brand','Year']) # 生成字段
s = groups['Total'].sum() # 对计算字段进行汇总
c = groups['ID'].count()
pt2 = pd.DataFrame({'Total':s ,'Count':c})
print(pt2)