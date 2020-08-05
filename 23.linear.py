import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

sales = pd.read_excel('/Users/Apple/Desktop/pandas/linear.xlsx', dtype={'Month': str})

slope, intercept, r, p, std_err = linregress(sales.index, sales.Revenue)

exp = sales.index * slope + intercept

plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='orange')
plt.title(f'y={slope}*X+{intercept}')
plt.xticks(sales.index, sales.Month, rotation=90)
plt.tight_layout()
plt.show()
