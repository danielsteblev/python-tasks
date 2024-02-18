def createNewList(list1, list2):
    result_list = []
    for el1 in list1:
        if el1 % 2 == 0 and list2.count(el1) == 0:
            result_list.append(el1)
    for el2 in list2:
        if el2 % 2 == 1 and list1.count(el2) == 0:
            result_list.append(el2)

    return result_list


#Чтение из файла
input_f = open('input.txt', 'r')
lines = input_f.readlines()
arg1 = [int(num) for num in lines[0].split(',')]
arg2 = [int(num) for num in lines[1].split(',')]
input_f.close()

#Запись в файл
output_f = open('output.txt', 'w')
output_f.write(str(createNewList(arg1, arg2)))
output_f.close()


