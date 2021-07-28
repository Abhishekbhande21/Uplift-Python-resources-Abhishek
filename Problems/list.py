
duplicate = [1,2,3, 2, 1,7,6,6,5,4]
final_list = []
for num in duplicate:
    if num not in final_list:
        final_list.append(num)

final_list.sort()
print(final_list)