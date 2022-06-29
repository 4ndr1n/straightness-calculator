import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file = input()

if file == "":
    file = "/Users/Andrin/Desktop/activity_8914463883.gpx"

file = open(file)
cont = file.readlines()
i = 0

set = re.findall("\"+(-?\d+(\.\d+)?)\s*", str(cont))


df = pd.DataFrame(set)
df.drop(columns=1, inplace=True)
df.drop([0,1],inplace=True)
df.reset_index(drop=True,inplace=True)

second_col = df[1::2]
second_col.dropna()
second_col.reset_index(drop=True,inplace=True)
df.drop(index=df.index[1::2],inplace=True)
df.dropna(inplace=True)
df.reset_index(drop=True,inplace=True)
df["long"] = second_col

df = df.astype(float, errors="raise")


print(df)

plt.plot(df)

def linear_calculation(x1, x2):
    z = x2[0] - x1[0] 
    y = x2[1] - x1[1]

n=0
x1 = 0
x2 = 0

for x in df.index:
    if x1 == 0:
        x1 = x
    elif x2 == 0:
        x2 = x
    else: 
        x2 = x1
        x1 = x

    # linear_calculation(x1, x2)


plt.show()