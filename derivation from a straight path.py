import re
import matplotlib.pyplot as plt
import pandas as pd
# import numpy as np

class getStuff:
    def getFile():
        
        ip = input("1:21. Juli, 2:26.Juni, 3:Sarnen, 4:30. Juni, enter:standard")
        
        if ip == 1:
            file = "/Users/Andrin/Desktop/GPX_data/21.\ Juli.gpx"
        
        if ip==2:
            file = "/Users/Andrin/Desktop/GPX_data/26.Juni.gpx"
        if ip==3:
            file = "/Users/Andrin/Desktop/GPX_data/Sarnen.gpx"
        elif ip==4:
            file = "/Users/Andrin/Desktop/GPX_data/30.\ Juni.gpx"

        else:
            file = "/Users/Andrin/Desktop/GPX_data/activity_8914463883.gpx"

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

    def getTwoValsUni(x1,x2,arr,count):
        if x1 == 0:
            x1 = arr[0]
            x2 = arr[1]
        else:
            x1 = x2
            x2 = arr[count]

    def getRelGrad(grad):
        varGradOT = []
        manualIndex = 0
        x1=0
        x2=0
        x1,x2=getStuff.getTwoVals(x1,x2,grad[0])

        

        for x in grad:
            manualIndex += 1
            #count = 2
            # x1,x2=getStuff.getTwoValsUni(x1,x2,grad,count)

            x1,x2=getStuff.getTwoVals(x1,x2,x)
            
            relGrad = x2-x1
            
            varGradOT.append(relGrad)
        #plt.plot(varGradOT)
        #plt.show()

        return relGrad

    def getOverOrUnder(x2,x1):
        OOU = False
        if x2 < x1:
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

    # Gives back gradient over the course of the route. It's a list of float numbers.
    def GradOverTime(lat,long):
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

    def noise(indexList):
        prunedIndex = []
        x1=0
        x2=0
        dif=0

        x1,x2 = getStuff.getTwoVals(x1,x2,indexList[0])

        for x in indexList:
            x1,x2 = getStuff.getTwoVals(x1,x2,x)
            if x1 == x:
                prunedIndex.append(x)
                pass
            else:
                dif = x2 - x1

            if dif > 50:
                prunedIndex.append(x)
            else:
                pass

        return prunedIndex

    def biggerOrNot(grad):
        storage = []
        x1=0
        x2=0
        x1, x2 = getStuff.getTwoVals(x1,x2,grad[0])

        for x in grad:
            x1,x2=getStuff.getTwoVals(x1,x2,x)
            storage.append(getStuff.getOverOrUnder(x2,x1))

        return storage

    def Turn(boolArr):
        counter = 0
        startIndex = []
        fuckingManualIndex = 0
        for x in boolArr:
            if x == False:
                counter += 1
            
            if counter == 30:
                startIndex.append(fuckingManualIndex)
                counter = 0
            
            fuckingManualIndex += 1
        
        index = find.noise(startIndex)

        return index


class export:

    def outToCsv(gradOverTime):
        f = open("/Users/Andrin/Desktop/boolArr.csv","w")

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

    gradOverTime = find.GradOverTime(lat,long)
    boolArr = find.biggerOrNot(gradOverTime)
    turn = find.Turn(boolArr)

    export.printGraph(x,y,turn)


if __name__ == "__main__":
    main()