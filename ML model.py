import re
import numpy as np
import pandas as pd


class getStuff:

    def getFile():
        ip = int(input("""1:21. Juli, 2:26.Juni, 3:Sarnen, 4:30. Juni, 0:standard
        """))
        
        files = {0:"/Users/Andrin/Desktop/GPX_data/activity_8914463883.gpx",
                1:"/Users/Andrin/Desktop/GPX_data/21. Juli.gpx",
                2:"/Users/Andrin/Desktop/GPX_data/26.Juni.gpx",
                3:"/Users/Andrin/Desktop/GPX_data/Sarnen.gpx",
                4:"/Users/Andrin/Desktop/GPX_data/30. Juni.gpx"}
        file = files.get(ip)
        return file

    def getData():
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

class ML:
    def dataprep(data):
        x = data['long']
        y = data['lat']
        print(x,data['lat'])



def main():
    print("hi")
    data = getStuff.getData()
    print(data)
    ML.dataprep(data)



if __name__ == "__main__()":
    main()