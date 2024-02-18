def createNewList(list1, list2):
    result_list = []
    for el in list1:
        if el % 2 == 0 and list2.count(el) == 0:
            result_list.append(el)
    for el in list2:
        if el % 2 == 1 and list1.count(el) == 0:
            result_list.append(el)

    result_list.sort()
    return result_list


#Чтение из файла
input_f = open('input-files/input_task1.txt', 'r')
lines = input_f.readlines()
arg1 = [int(num) for num in lines[0].split(',')]
arg2 = [int(num) for num in lines[1].split(',')]
input_f.close()

#Запись в файл
output_f = open('output-files/output_task1.txt', 'w')
output_f.write(str(createNewList(arg1, arg2)))
output_f.close()


