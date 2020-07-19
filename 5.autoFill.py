import pandas as pd
from datetime import date, timedelta  # 使用timedelta实现天数加减


# 定义月份递增的函数
# start:开始时间 i:增加的月份
def monthAdd(start, i):
    # 首先读取开始时间的年月
    year = start.year
    month = start.month + i
    day = start.day
    if month > 12:
        year = year + month // 12  # 满几年，加几年
        month = month % 12
    return date(year, month, day)  # 因为日期对象没办法直接覆盖，只能重新创建


'并没有跳过空行空列,通过参数跳过3个空行，并读取C～F'
books = pd.read_excel('/Users/apple/Desktop/Books.xlsx', skiprows=3, usecols='C:F',
                      index_col=None, dtype={'ID': str, 'InStore': str, 'Date': str})

start_date = date(2020, 1, 1)
'用迭代循环，填充'
for i in range(0, 20):
    # 使用at方法，给Series赋值
    books['ID'].at[i] = i + 1
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'no'
    books['Date'].at[i] = start_date + timedelta(days=i)
    books['Date'].at[i] = monthAdd(start_date, i)

'直接在DataFrame上修改单元格的值,第i行，某一列'
books.at[0, 'ID'] = 100

'当一开始没有数据的时候，会显示NaN(Not A Number)，pandas会将这一列的类型设置为float'
'可以在读取Excel的时候指定某个列的数据类型，当数据是NaN的时候，不允许float转为int，需要转为str'
print(books)
