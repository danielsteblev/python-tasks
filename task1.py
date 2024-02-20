def create_list(list1, list2):
    result_list = []
    for el in list1:  # check 1st list
        if el % 2 == 0 and list2.count(el) == 0:
            result_list.append(el)
    for el in list2:  # check 2nd list
        if el % 2 == 1 and list1.count(el) == 0:
            result_list.append(el)

    result_list.sort()  # sort result_list

    return result_list


arg1 = []
arg2 = []


try:  # read lists from file
    input_f = open('input-files/input_task1.txt', 'r')
    lines = input_f.readlines()
    arg1 = [int(num) for num in lines[0].split(',')]
    arg2 = [int(num) for num in lines[1].split(',')]
    input_f.close()
except FileNotFoundError as err:  # throw exception if file not found
    print("File not found or it cannot be read!")
    print(err)


output_f = open('output-files/output_task1.txt', 'w')  # write result_list to file
output_f.write(str(create_list(arg1, arg2)))
output_f.close()



