s = input("Введите строку: ")
print("Строка без 3 символа: ")
for i in range(len(s)):
    if i == 2:
        continue
    print(s[i], end="")
if "c" in s:
    print("\nВ строке есть символ 'c'")
print("Длина строки:", len(s))
print("Строка без последнего символа:", s[:-1])
