import pandas as pd

books = pd.read_excel('/Users/apple/Desktop/Total.xlsx',
                      skiprows=2, usecols='C:F', index_col='ID',
                      dtype={'Total': str})

# 直接操作列，列运算（操作符重载）
books['Total'] = books['Price'] * books['Mount']

# 使用Series的apply()方法，对Series中的每个元素进行函数运算
books['Total'] = books['Total'].apply(lambda x: x + 10)

print(books['Total'])
