carList = [4,1,3,2]
overtake = 0

for i in range(len(carList)):
    for j in range(0,len(carList)):
        if (carList[i] > carList[j]):
            carList[i],carList[j]=carList[j],carList[i]
            overtake= overtake+1
print("Number of overtakes are:"+str(overtake))
    
