import re
import matplotlib.pyplot as plt
import pandas as pd
# import numpy as np

class getStuff:
    def getFile():
        ip = input()

        file = "/Users/Andrin/Desktop/" + ip

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

    def getRelGrad(grad):
        x1 = 0
        x2 = 0
        dif = 0
        varGradOT = []
        x1,x2=getStuff.getTwoVals(x1,x2,grad[0])

        for x in grad:
            manualIndex += 1

            x1,x2=getStuff.getTwoVals(x1,x2,x)
            
            relGrad = x2-x1
            
            varGradOT.append(relGrad)
    
        
        #plt.plot(varGradOT)
        #plt.show()


        return relGrad

    def getOverOrUnder(x2,x1):
        OOU = False
        if x2 > x1:
            OOU = True
        else:
            OOU = False

        return OOU


class  find:
    def gradient_calculator(x_y_val):
        z = []
        x1=0
        x2=0
        x1, x2 = getStuff.getTwoVals(x1,x2,x_y_val[0])
        for x in x_y_val:
            x1, x2 = getStuff.getTwoVals(x1,x2,x)
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
        varGrad =0
        manualIndex = 0

        relGrad = getStuff.getRelGrad(grad)

        if relGrad > 3 or relGrad < -3:
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
        
        print(prunedIndex)
        return prunedIndex

    def findRelation(grad):
        x1,x2 = getStuff.GetTwoVals(x1,x2,grad[0])
        





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