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


def Turn(boolArr):
    # attempt 2
    countUp = 0
    countDown = 0
    startIndex = []
    fuckingManualIndex = 0
    for x in boolArr:
        if x == False:
            countUp += 1
            countDown = 0
        else:
            countDown += 1
            countUp = 0

        if countUp == 6 or countDown == 6:
            startIndex.append(fuckingManualIndex)
            countUp = 0
            countDown = 0

        
        fuckingManualIndex += 1
    
    index = find.noise(startIndex)

    return index

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

def getOverOrUnder(x2,x1):
    # attempt 2
    OOU = False
    if x2 > x1:
        OOU = True
    else:
        OOU = False
    return OOU


"""