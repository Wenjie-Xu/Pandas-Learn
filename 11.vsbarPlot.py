import pandas as pd
import matplotlib.pyplot as plt

platforms = pd.read_excel('/Users/apple/Desktop/pandas/vsbar.xlsx',
                          skiprows=1, usecols='B:D')

'使用oandas作图'
# 先对数据排序
platforms.sort_values(by=2020, ascending=False, inplace=True)
platforms.plot.bar(x='Platform', y=[2019, 2020],
                   color=['orange', 'red'])

'使用matplotlib对图标进行修饰'

# 设置标题，字体，加粗
plt.title('Sales Plot', fontsize=16, fontweight='bold')
# 设置轴标签
plt.xlabel('platform', fontweight='bold')
plt.ylabel('sells', fontweight='bold')

# 获得坐标轴
ax=plt.gca()
# 重新设置x轴，包括文字，顺时针旋转45度，围绕文字中心，通过参数可以改变这个中心
ax.set_xticklabels(platforms['Platform'],rotation=45,ha='right')

# 获得当前的图形
f=plt.gcf()
# 子表位置调整
f.subplots_adjust(left=0.2, bottom=0.1)
plt.show()
print(platforms)
