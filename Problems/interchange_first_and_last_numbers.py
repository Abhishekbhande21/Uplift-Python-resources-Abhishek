"""
[12,35,9,56,24]
[24,35,9,56,12]
"""
"""
The first approach is to find the length of the list and simply swap the two elements
No, how to swap two elements.
For that the best and easiest solution (not the most efficient) is to take another variable as a temp variable
"""


def intFirstLast(myList):
    sizeOfList = len(myList)
    # Swapping of the elements
    tempVar = myList[0]
    myList[0] = myList[sizeOfList - 1]
    myList[sizeOfList - 1] = tempVar
    return myList


def intFirstLastSecondApproach(myList):
    # Swapping of the elements
    tempVar = myList[0]
    myList[0] = myList[-1]
    myList[-1] = tempVar
    return myList


def intFirstLastXYApproach(myList):
    myList[0], myList[-1] = myList[-1], myList[0]
    return myList


def intFirstLastStarOperand(myList):
    a, *b, c = myList
    myList = [c, *b, a]
    return myList


# Main Part of the Code / Driver Section of the Code
newList = [15, 15, 12, 26, 4, 8, 9, 396]
print(intFirstLast(newList))
newList = [15, 15, 12, 26, 4, 8, 9, 396]
print(intFirstLastSecondApproach(newList))
newList = [15, 15, 12, 26, 4, 8, 9, 396]
print(f"Using the , switch method: {intFirstLastXYApproach(newList)}")
newList = [15, 15, 12, 26, 4, 8, 9, 396]
print(f"Using the * operand approach: {intFirstLastStarOperand(newList)}")