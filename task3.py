def max_sum_of_segments(input_segments):
    input_segments.sort(key=lambda x: (x[1], x[1] - x[0]), reverse=True)
    total_sum = 0
    selected_segments = []

    for i in range(len(input_segments)):
        if len(selected_segments) >= 3:
            return total_sum, selected_segments

        # если список - пустой
        # или правая координата текущего отрезка меньше чем левая координата последнего выбранного
        if not selected_segments or input_segments[i][1] < selected_segments[-1][0]:
            total_sum += input_segments[i][1] - input_segments[i][0]  # находим длину отрезка: правая - левая координата
            selected_segments.append(input_segments[i])

    return total_sum, selected_segments


segments = []
try:  # read lists from file
    input_f = open('input-files/input_task3.txt', 'r')
    segments = [[int(num) for num in line.split(',')] for line in input_f]
    input_f.close()

except FileNotFoundError as err:  # throw exception if file not found
    print("File not found or it cannot be read!")
    print(err)

result, selected_segments = max_sum_of_segments(segments)
output_f = open('output-files/output_task3.txt', encoding='utf-8', mode='w')  # write result_list to file
if len(selected_segments) < 3:
    output_f.write("Exception: количество найденных отрезков < 3!")
else:
    output_f.write("Максимальная сумма длин отрезков: " + str(result))
    output_f.write("\nВыбранные отрезки: " + str(selected_segments))
output_f.close()
