import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('/Users/apple/Desktop/pandas/everymonth.xlsx', index_col='ID')
# 添加计算列
users['Total'] = users.Jan + users.Feb + users.Mar
# 对计算列进行排序
users.sort_values(by='Total', ascending=True, inplace=True)
# 使用pandas进行作图（stacked：叠加 / users.plot.barh：水平显示）
users.plot.barh(x='Name', y=['Jan', 'Feb', 'Mar'], stacked=True)
plt.title('Everyone Come Situation', fontsize=18, fontweight='bold')
# 紧凑显示，防止标签显示不全
plt.tight_layout()
plt.show()
print(users)
