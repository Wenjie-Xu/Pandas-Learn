import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('/Users/apple/Desktop/pandas/pie.xlsx', index_col='From')

# 做饼图只要一个Series即可，且图例使用的是index，因此需要指明
# 如果不想手动排序，加上一个参数：counterclock=True即可（像时钟一样）
# startangle = -270：起始角度
students['2017'].sort_values(ascending=True).plot.pie(fontsize=10, startangle=-270)

plt.title('US Students Constitute', fontsize=16, fontweight='bold') # 设置标题
plt.ylabel('2017', fontsize=12, fontweight='bold') # 设置y轴
plt.show()

print(students)
