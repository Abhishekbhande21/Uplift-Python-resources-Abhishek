#calculate how many integers, strings, in the list 

test_list = [3, 'computer', True, False, 5, 'geeks', 6, 7, 2.3, 6.5]
print("The original list is : " + str(test_list))
intCount = len(list(i for i in test_list if isinstance(i, int)))
strCount = len(list(i for i in test_list if isinstance(i, str)))
boolCount = len(list(i for i in test_list if isinstance(i, bool)))
floatCount = len(list(i for i in test_list if isinstance(i, float)))
print("The length of integers in list is : " + str(intCount))
print("The length of floats in list is : " + str(floatCount))
print("The length of booleans in list is : " + str(boolCount))
print("The length of strings in list is : " + str(strCount))