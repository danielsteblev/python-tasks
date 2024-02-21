def counter(arg):
    count = 0
    max = 0
    for el in arg:
        if el == 1:
            count+=1
        else:
            count = 0

        max = count

    return max


arg = [0, 1, 1, 0, 0, 1, 1, 1]
print(arg)
print(counter(arg))
