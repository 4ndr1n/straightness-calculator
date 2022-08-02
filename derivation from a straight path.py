import re
import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd
class getStuff:

    def getFile():
        ip = int(input("""1:21. Juli, 2:26.Juni, 3:Sarnen, 4:30. Juni, 0:standard
        """))
        if ip  == 0:
            file = "/Users/Andrin/Desktop/GPX_data/activity_8914463883.gpx"
        elif (ip == 1):
            file = "/Users/Andrin/Desktop/GPX_data/21. Juli.gpx"
        elif (ip==2):
            file = "/Users/Andrin/Desktop/GPX_data/26.Juni.gpx"
        elif (ip==3):
            file = "/Users/Andrin/Desktop/GPX_data/Sarnen.gpx"
        elif (ip==4):
            file = "/Users/Andrin/Desktop/GPX_data/30. Juni.gpx"
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
        # attempt 1 used unmodified for attempt 2
        if x1 == 0:
            x1 = x
        elif x2 == 0:
            x2 = x
        else: 
            x1 = x2
            x2 = x
        return x1, x2

    def getTwoValsUni(x1,x2,arr,count):
        # test
        if x1 == 0:
            x1 = arr[0]
            x2 = arr[1]
        else:
            x1 = x2
            x2 = arr[count]

    def getOverOrUnder(x2,x1):
        # attempt 2
        OOU = False
        if x2 > x1:
            OOU = True
        else:
            OOU = False
        return OOU


class  find:
    def gradient_calculator(x,y):
        z = []
        for i in range(x.count()):
            z.append(x[i]/y[i])
        return z

    def noise(indexList):
        #attempt 2
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

            if dif > 10:
                prunedIndex.append(x)
            else:
                pass

        return prunedIndex

    def biggerOrNot(grad):
        # attempt 2
        storage = []
        x1=0
        x2=0
        x1, x2 = getStuff.getTwoVals(x1,x2,grad[0])

        for x in grad:
            x1,x2=getStuff.getTwoVals(x1,x2,x)
            storage.append(getStuff.getOverOrUnder(x2,x1))

        return storage

    def Turn(boolArr):
        startIndex = []
        fuckingManualIndex = 0
        switch = False
        prevT = False
        prevF = True
        for x in boolArr:
            if x == switch and switch == False:
                switch = True
                if prevF == x:
                    startIndex.append(fuckingManualIndex)
                prevF = x
            elif (x == switch and switch == True):
                switch = False
                
                if prevT == x:
                    startIndex.append(fuckingManualIndex)
                prevT = x
            
            fuckingManualIndex += 1
        
        # index = find.noise(startIndex)

        return startIndex


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
    grad = find.gradient_calculator(x,y)

    z = find.biggerOrNot(grad)
    Index = find.Turn(z)
    export.printGraph(x,y,Index)


if __name__ == "__main__":
    main()