try:
    a = int(input('Введите не отрифательное число:\n'))
    if abs(a) != a:
        print('Число отрицательное')
        exit()
    b = 1
    for i in range(1, a+1):
        b *= i
    print(b)
except ValueError:
    print('Неверный формат данных')
