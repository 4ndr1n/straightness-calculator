from itertools import count
from operator import index
import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def getFile():
    file = input()

    if file == "":
        file = "/Users/Andrin/Desktop/activity_8914463883.gpx"
    return file

def getData():
    i = 0
    file = open(getFile())
    cont = file.readlines()

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

    lat = gradient_calculator(x)
    long = gradient_calculator(y)
    return lat,long

def getTwoVals(x1,x2,x):
    if x1 == 0:
        x1 = x
    elif x2 == 0:
        x2 = x
    else: 
        x1 = x2
        x2 = x
    return x1, x2

def gradient_calculator(x_y_val):
    z = []
    x1=0
    x2=0
    for x in x_y_val:
        x1, x2 = getTwoVals(x1,x2,x)
        if x1 == x:
            pass
        else:
            d = x2 - x1    
            z.append(d)
    return z

def findGradOverTime(lat,long):
    gradOverTime = []
    n = 0
    for x in lat:
        n += 1

    for x in range(n):
        if long[x] == 0 or long[x] == 0.0:
            pass
        else:
            gradOverTime.append(lat[x] / long[x])
    return gradOverTime

def findTurn(grad):
    manualIndex = 0
    indexList = []
    prunedIndex = []
    x1 = 0
    x2 = 0
    dif = 0

    for x in grad:
        manualIndex += 1
        if x < 0:
            indexList.append(manualIndex)
    for x in indexList:
        x1,x2 = getTwoVals(x1,x2,x)
        if x1 == x:
            prunedIndex.append(x)
            pass
        else:
            dif = x2 - x1

        if dif > 20:
            prunedIndex.append(x)
        else:
            pass
    print(prunedIndex)


def main():
    lat, long = getData()
    gradOverTime = findGradOverTime(lat,long)
    turn = findTurn(gradOverTime)


if __name__ == "__main__":
    main()