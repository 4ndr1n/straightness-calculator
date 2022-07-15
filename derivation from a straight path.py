import re
import matplotlib.pyplot as plt
import pandas as pd
# import numpy as np

class getStuff:
    def getFile():
        file = input()

        if file == "":
            file = "/Users/Andrin/Desktop/activity_8914463883.gpx"
        return file

    def getData():
        i = 0
        file = open(getStuff.getFile())
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

        return x,y

    def getTwoVals(x1,x2,x):
        if x1 == 0:
            x1 = x
        elif x2 == 0:
            x2 = x
        else: 
            x1 = x2
            x2 = x
        return x1, x2

class  find:
    def gradient_calculator(x_y_val):
        z = []
        x1=0
        x2=0
        for x in x_y_val:
            x1, x2 = getStuff.getTwoVals(x1,x2,x)
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
        # export.outToCsv(gradOverTime)
        return gradOverTime

    def findTurn(grad):
        indexList = []
        prunedIndex = []
        varGradOT = []
        absGradOT = []
        varGrad =0
        manualIndex = 0
        x1 = 0
        x2 = 0
        dif = 0

        for x in grad:
            manualIndex += 1
            x1,x2=getStuff.getTwoVals(x1,x2,x)
            
            if x2 == 0:
                getStuff.getTwoVals(x1,x2,x)
            varGradOT.append(x2-x1)
            varGrad = x2-x1
            absGrad = abs(varGrad)
            absGradOT.append(absGrad)
            if absGrad > 14:
                pass
            elif absGrad > 0.1:
                indexList.append(manualIndex)
        for x in indexList:
            x1,x2 = getStuff.getTwoVals(x1,x2,x)
            if x1 == x:
                prunedIndex.append(x)
                pass
            else:
                dif = x2 - x1

            if dif > 10:
                prunedIndex.append(x)
            else:
                pass
        plt.plot(absGradOT)
        plt.show()
        
        print(prunedIndex)
        return prunedIndex

class export:

    def outToCsv(gradOverTime):
        f = open("/Users/Andrin/Desktop/sarnen.csv","w")

        for x in gradOverTime:
            y = str(x)
            z = y + "\n"
            f.write(z)
        f.write(gradOverTime)

    def printGraph(x,y,turn):
        xm = []
        ym = []
        n=0
        for n in turn:
            xm.append(x[n])
            ym.append(y[n])

        plt.scatter(xm,ym,color='k')
        plt.plot(x,y,color='g')
        plt.show()



def main():
    x,y = getStuff.getData()
    lat = find.gradient_calculator(x)
    long = find.gradient_calculator(y)

    gradOverTime = find.findGradOverTime(lat,long)
    turn = find.findTurn(gradOverTime)
    export.printGraph(x,y,turn)


if __name__ == "__main__":
    main()