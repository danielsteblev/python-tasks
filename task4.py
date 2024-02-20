import re


def create_new_string(input_text):
    new_str = ''
    # составляем новый список слов и символов
    words = re.findall(r'[a-zA-Zа-яА-Я0-9]+|[^a-zA-Zа-яА-Я0-9]+', input_text)
    for word in words:
        if re.match(r'[a-zA-Zа-яА-Я0-9]+', word):  # если это слово, то переворачиваем
            new_str += reverse_letters(word)
        else:  # если символ - просто оставляем на том же месте
            new_str += word

    return new_str


def reverse_letters(word):  # функция для "переворачивания" слова
    new_world = ''
    chars = list(word)
    index = len(chars)
    for char in chars:
        index -= 1
        new_world += chars[index]

    return new_world


try:  # read lists from file
    input_f = open('input-files/input_task4.txt', encoding='utf-8', mode='r')
    file_text = str(input_f.readlines())
    input_f.close()
except FileNotFoundError as err:  # throw exception if file not found
    print("File not found or it cannot be read!")
    print(err)

output_f = open('output-files/output_task4.txt', encoding='utf-8', mode='w')  # write result_list to file
output_f.write(create_new_string(file_text))
output_f.close()
