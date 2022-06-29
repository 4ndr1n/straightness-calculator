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
df.columns = ['lat']
df["long"] = second_col

df = df.astype(float, errors="raise")

x = df.loc[:,"lat"]
y = df.loc[:,"long"]

# plt.plot(x,y)
n=0

def gradient_calculator(x_y_val):
    x1 = 0
    x2 = 0
    z = []
    for x in x_y_val:
        if x1 == 0:
            x1 = x
        elif x2 == 0:
            x2 = x
        else: 
            x1 = x2
            x2 = x
        z.append(x2 - x1)
    return z

lat = gradient_calculator(x)
long = gradient_calculator(y)

for x in lat:
    for y in long:
        z = x / y
        

print(z)

plt.show()