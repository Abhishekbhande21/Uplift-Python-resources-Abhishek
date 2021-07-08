carList = [4,3,1,2]
overtake = 0

for i in range(len(carList)):
    for j in range(0,len(carList)):
        if (carList[i] > carList[j]):
            i , j = j , i
            overtake= overtake+1
print("Number of overtakes are:"+str(overtake))
    
