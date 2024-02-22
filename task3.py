def max_sum_of_segments(segments):
    segments.sort(key=lambda x: x[1])  # сортируем отрезки по правому концу
    total_sum = 0
    selected_segments = []

    for i in range(len(segments)):
        if len(selected_segments) >= 3:
            return total_sum, selected_segments

        # если список - пустой
        # или левая координата текущего отрезка больше чем конец последнего выбранного
        if not selected_segments or segments[i][0] > selected_segments[-1][1]:
            total_sum += segments[i][1] - segments[i][0]  # находим длину отрезка: правая - левая координата
            selected_segments.append(segments[i])

    return total_sum, selected_segments


try:  # read lists from file
    input_f = open('input-files/input_task3.txt', 'r')
    segments = [[int(num) for num in line.split(',')] for line in input_f]
    input_f.close()

except FileNotFoundError as err:  # throw exception if file not found
    print("File not found or it cannot be read!")
    print(err)

result, selected_segments = max_sum_of_segments(segments)
output_f = open('output-files/output_task3.txt', encoding='utf-8', mode='w')  # write result_list to file
if(len(selected_segments) < 3):
    output_f.write("Exception: количество найденных отрезков < 3!")
else:
    output_f.write("Максимальная сумма длин отрезков: " + str(result))
    output_f.write("\nВыбранные отрезки: " + str(selected_segments))
output_f.close()

