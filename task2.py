def overlay_arrays(arr1, arr2):
    rows1, cols1 = len(arr1), len(arr1[0])
    rows2, cols2 = len(arr2), len(arr2[0])

    for i in range(rows1 - rows2 + 1):
        for j in range(cols1 - cols2 + 1):
            match = True
            for k in range(rows2):
                for l in range(cols2):
                    if arr1[i + k][j + l] != arr2[k][l]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return (i, j)

    return None

arr1 = []
arr2 = []
current = arr1

try:  # read lists from file
    input_f = open('input-files/input_task2.txt', 'r')
    for line in input_f.readlines():
        if ',' not in line:
            current = arr2
        else:
            current.append([])
            for x in line.split(','):
                (current[len(current)-1]).append(int(x))
    print(arr1)
    print(arr2)
    input_f.close()
except FileNotFoundError as err:  # throw exception if file not found
    print("File not found or it cannot be read!")
    print(err)

result = overlay_arrays(arr1, arr2)
output_f = open('output-files/output_task2.txt', encoding='utf-8', mode='w')  # write result_list to file
if result:
    output_f.write("Координаты ячейки:" + str(result))
else:
    output_f.write("Массивы наложить нельзя!")
output_f.close()
