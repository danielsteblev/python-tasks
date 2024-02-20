import re
text = "Помимо C# вы будете изучать Java, C++ и другие языки программирования."

words = re.findall(r'[a-zA-Zа-яА-Я0-9]+|[^a-zA-Zа-яА-Я0-9]+', text)

print(words)