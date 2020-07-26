'散点图、直方图、密度图'

# 直方图可以看出分布情况
import pandas as pd
import matplotlib.pyplot as plt

homes = pd.read_excel('/Users/Apple/Desktop/pandas/home_data.xlsx')
pd.options.display.max_columns = 777 # 修改最大显示列数
print(homes.head())

'散点图（scatter）'
homes.plot.scatter(x='sqft_living',y='price')

'直方分布图（hist）'
homes.sqft_living.plot.hist(bins=100) # 设置分布区间
plt.xticks(range(0,max(homes.sqft_living),500),rotation=90) # 用range生成一个标签序列，并且旋转90度

'密度图，组成的占比（Kernel Destiny Estimation）'
homes.sqft_living.plot.kde()
plt.xticks(range(0,max(homes.sqft_living),500),rotation=90) # 用range生成一个标签序列，并且旋转90度
plt.show()

