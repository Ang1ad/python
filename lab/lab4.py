while True:
    operation = input("Введите операцию: ")
    if operation == "quit":
        print("Выход")
        break
    firstNum = int(input("Введите первое число: "))
    secondNum = int(input("Введите второе число: "))
    res = 0
    match operation:
        case '+':
            res = firstNum + secondNum
            print("Результат: ", res)
        case '-':
            res = firstNum - secondNum
            print("Результат: ", res)
        case '/':
            while (secondNum == 0):
                print ("На 0 делить нельзя")
                secondNum = int(input("Введите второе число: "))
            res = firstNum / secondNum
            print("Результат: ", res)
        case '*':
            res = firstNum * secondNum
            print("Результат: ", res)

