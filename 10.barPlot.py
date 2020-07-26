import pandas as pd
import matplotlib.pyplot as plt

student = pd.read_excel('/Users/apple/Desktop/pandas/pic1.xlsx',
                        skiprows=3,usecols='D:E',index_col=None)
student.sort_values(by='Num', ascending=True, inplace=True)
# 使用pands自带的模块进行作图
# student.plot.bar(x='Item',y='Num',color='green',title='mings score')

#使用matplotlib进行柱形图作图
plt.bar(student.Item, student.Num,color='green')
plt.xlabel('Item') #设置轴名
plt.ylabel('Num')
plt.title('mings score', fontsize=16)
plt.xticks(student.Item, rotation='90')

# 使用matplotlib进行图的渲染
plt.tight_layout() # 紧凑显示
plt.show()
print(student)