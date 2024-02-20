import re


def create_new_string(input):
    new_str = ''
    # составляем новый список слов и символов
    words = re.findall(r'[a-zA-Zа-яА-Я0-9]+|[^a-zA-Zа-яА-Я0-9]+', input)
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


str = "Помимо C# вы будете изучать Java, C++ и другие языки программирования."
print(create_new_string(str))
