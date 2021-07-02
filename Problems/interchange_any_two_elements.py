"""
[12,35,9,56,24]
[24,35,9,56,12]
"""
"""
The first approach is to find the length of the list and simply swap the two elements
No, how to swap two elements.
For that the best and easiest solution (not the most efficient) is to take another variable as a temp variable
"""


def swapEl(myList, pos1, pos2):
    sizeOfList = len(myList)
    # Swapping of the elements
    tempVar = myList[pos1]
    myList[pos1] = myList[pos2]
    myList[pos2] = tempVar
    return myList


def swapElSecondApproach(myList, pos1, pos2):
    # Swapping of the elements
    tempVar = myList[pos1]
    myList[pos1] = myList[pos2]
    myList[pos2] = tempVar
    return myList


def swapElXYApproach(myList, pos1, pos2):
    myList[pos1], myList[pos2] = myList[pos2], myList[pos1]
    return myList


def swapElStarOperand(myList, pos1, pos2):
    a, *b, c = myList
    myList = [c, *b, a]
    return myList


# Main Part of the Code / Driver Section of the Code
newList = [15, 15, 12, 26, 4, 8, 9, 396]
print(swapEl(newList, 0, 3))
newList = [15, 15, 12, 26, 4, 8, 9, 396]
print(swapElSecondApproach(newList, 3, 4))
newList = [15, 15, 12, 26, 4, 8, 9, 396]
print(f"Using the , switch method: {swapElXYApproach(newList,1,5)}")
newList = [15, 15, 12, 26, 4, 8, 9, 396]
print(f"Using the * operand approach: {swapElStarOperand(newList,1,2)}")