def createNewList(list1, list2):
    result_list = []
    for el1 in list1:
        if el1 % 2 == 0 and list2.count(el1) == 0:
            result_list.append(el1)
    for el2 in list2:
        if el2 % 2 == 1 and list1.count(el2) == 0:
            result_list.append(el2)

    return result_list

#arg1 = [2, 4, 6, 7, 11]
#arg2 = [1, 3, 4, 2, 9, 11]
# result_list = [6, 1, 3]

arg1 = []
arg2 = []
f = open('input.txt', 'r')
lines = f.readlines()
arg1 = [int(num) for num in lines[0].split(',')]
arg2 = [int(num) for num in lines[1].split(',')]
print(arg1)
print(arg2)

f.close()

print(createNewList(arg1, arg2))

