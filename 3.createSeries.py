import pandas as pd

# 创建一个序列
s1 = pd.Series()

# 通过字典转换为序列
d = {'x': 100, 'y': 200, 'z': 300}
s2 = pd.Series(d)  # 将字典的k-v转为series的k-v

# 预先设置好index和value
value = [100, 200, 300]
index = ['x', 'y', 'z']

s3 = pd.Series(value, index=index)

print(s2)
print(s2.index)
print(s3)

'当使用不同的方法将series添加到dataframe中，将确定series属于行还是列'
