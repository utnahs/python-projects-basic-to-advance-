numbers_list=[85,66,99,100]
temp=numbers_list[0]
for num in numbers_list:
    if num > temp:
        temp=num
print(temp)