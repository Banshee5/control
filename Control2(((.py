list = []
while True:
    num = int(input('Введите числа: '))
    list += [num]
    if num == 0:
        break

print(*sorted(list))
