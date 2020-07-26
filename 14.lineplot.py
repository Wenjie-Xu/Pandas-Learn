# 折线图

import pandas as pd
import matplotlib.pyplot as plt

bikes = pd.read_excel('/Users/Apple/Desktop/pandas/bikeline.xlsx', index_col='Week')
print(bikes.index)

'''
叠加区域图，通过面积看出组成最大面积的各个部分
比叠加柱形图可以看出变化的趋势
'''

bikes.plot(y=list(bikes.columns)) # 折线图
bikes.plot.area(y=list(bikes.columns)) # 叠加区域图

plt.tight_layout()
plt.title('Sale Trend', fontsize=12, fontweight='bold')
plt.ylabel('Total', fontsize=10, fontweight='bold') # 设置标签
plt.xticks(bikes.index, fontsize=8) # 设置符号
plt.show()
