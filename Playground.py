if -1 < 0:
    print("hi")

def main():
    print("Yeah")


if __name__ == "__main__":
    main()



# Print a csv of the data
"""
    print(gradOverTime)
f = open("/Users/Andrin/Desktop/new.csv","w")

for x in gradOverTime:
    y = str(x)
    z = y + "\n"
    f.write(z)
f.write(gradOverTime)

# retired code
def GradOverTime(lat,long):
    # attempt 1 
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


    def getRelGrad(grad):
        # attempt 1
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
    


"""