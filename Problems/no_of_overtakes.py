  
carList = [4, 1, 2, 5]
overtake = 0

for i in range(len(carList)):
    for j in range(i+1, len(carList)):
        if(carList[j] < carList[i]):
            overtake += 1

print(overtake)