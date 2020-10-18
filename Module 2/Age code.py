import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = r'D:\Work\KPMG\Module 2\Clear data.xlsx'
df1 = pd.read_excel(file, 'Newcustomer')

bin = np.linspace(min(df1["Age"]), max(df1["Age"]), 4)
group = ["1", "2", "3"]
df1["age-binned"] = pd.cut(df1["Age"], bin, labels=group, include_lowest=True)
#print(df1["age-binned"])

x = df1["state"]
y = df1["Value"]
plt.xlabel('States')
plt.ylabel('Value')
plt.ylim()
#plt.hist(df1["Age"], bin, histtype='bar', rwidth=0.8 )
plt.scatter(x, y)
plt.show()

