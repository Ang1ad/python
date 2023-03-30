a = int(input("Введите произвольное число: "))
b = int(input("Введите пограничное число: "))
if (a < b):
    print('{} меньше {}'.format(a, b))
if (a > b):
    print('{} больше {}'.format(a, b))
    if (a > 3 * b):
        print('{} больше {} более, чем в 3 раза'.format(a, b))
