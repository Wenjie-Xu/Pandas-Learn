import pandas as pd

books = pd.read_excel('/Users/apple/Desktop/Total.xlsx',skiprows=2,usecols='C:F',
                      dtype={'Worth':str},index_col='ID')

# DataFrame的sort_value方法，接收的两个参数，一个是排序的列，一个是排序的方式
# 多列可以使用list，各自指定排序方式
books.sort_values(by=['Price','Worth'], ascending=[False,True], inplace=True)
print(books)