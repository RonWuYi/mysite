my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    for j in range(len(my_list[i+1:])):
        # print(f'i is {my_list[i]}')
        print(f'j is {my_list[i+1:][j]}')
# print(len(my_list))
# print(ord('9'))