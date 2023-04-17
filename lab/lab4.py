from math import acos, factorial
from random import uniform

print("Вам доступны функции: '+', '-', '/', '*', '^' - возведение в степень, 'arccos' - арккосинус, 'module' - модуль, '!' - факториал, 'random' - случайное число.")
print("Чтобы выйти, введите 'quit'.")

while True:
    operation = input("Введите операцию: ")
    if operation == "quit":
        print("Выход")
        break
    res = 0
    match operation:
        case '+':
            firstNum = float(input("Введите первое число: "))
            secondNum = float(input("Введите второе число: "))
            res = firstNum + secondNum
            print("Результат: ", res)
        case '-':
            firstNum = float(input("Введите первое число: "))
            secondNum = float(input("Введите второе число: "))
            res = firstNum - secondNum
            print("Результат: ", res)
        case '/':
            firstNum = float(input("Введите первое число: "))
            secondNum = float(input("Введите второе число: "))
            while (secondNum == 0):
                print ("На 0 делить нельзя")
                secondNum = int(input("Введите второе число: "))
            res = firstNum / secondNum
            print("Результат: ", res)
        case '*':
            firstNum = float(input("Введите первое число: "))
            secondNum = float(input("Введите второе число: "))
            res = firstNum * secondNum
            print("Результат: ", res)
        case '^':
            firstNum = float(input("Введите первое число: "))
            secondNum = float(input("Введите второе число: "))
            res = firstNum ** secondNum
            print("Результат: ", res)
        case 'arccos':
            firstNum = float(input("Введите число: "))
            if abs(firstNum) <= 1:
                res = acos(firstNum)
                print("Результат: ", res)
            else:
                print("Данного арккосинуса не существует.")
        case '!':
            firstNum = int(input("Введите число: "))
            res = factorial(firstNum)
            print("Результат: ", res)
        case 'random':
            firstNum = float(input("Введите левую границу: "))
            secondNum = float(input("Введите правую границу: "))
            res = uniform(firstNum, secondNum)
            print("Результат: ", res)
        case 'module':
            firstNum = float(input("Введите число: "))
            res = abs(firstNum)
            print("Результат: ", res)


