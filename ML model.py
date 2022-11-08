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
    def dataprep(x,y):
        y = np.array(y)
        x = np.array(x)
        data = np.stack((x,y),axis=0)

        m,n = data.shape
        
        data_dev = data[0:3,0:100].T
        
        X_dev = data_dev[0:100,0]
        Y_dev = data_dev[0:100,1]
        
        data_train = data[0:3,100:n]
        X_train = data_train[0]
        Y_train = data_train[1]


        return X_dev, Y_dev, X_train, Y_train

    def init_params():
        W1 = np.random.rand(10, 784) -0.5
        b1 = np.random.rand(10,1) -0.5
        W2 = np.random.rand(10,10) - 0.5
        b2 = np.random.rand(10,1) - 0.5
        return W1,b1,W2,b2

    def ReLU(Z):
        return np.maximum(Z,0)

    def forward_prop(W1,b1,W2,b2,X):
        Z1 = W1.dot(X) + b1
        A1 = ML.ReLU(Z1)
        Z2 = W2.dot(A1) + b2
        A2 = ML.ReLU(Z2)
        return Z1, A1, Z2, A2


    def ReLU_deriv(Z):
        return Z > 0

    
    def back_prop(Z1,A1,Z2,A2,W2,X,Y,m):
        dZ2 = ML.ReLU_deriv(Z2) - Y
        dW2 = 1 / m * dZ2.dot(A1.T)
        db2 = 1 / m * np.sum(dZ2)
        dZ1 = W2.T.dot(dZ2) * ML.ReLU_deriv(Z1)
        dW1 = 1 / m * dZ1.dot(X.T)
        db1 = 1 / m * np.sum(dZ1)
        return dW1, db1, dW2, db2

        


def main():
    x,y = getStuff.getData()
    X_dev,Y_dev,X_train,Y_train = ML.dataprep(x,y)

if __name__ == "__main__":
    main()