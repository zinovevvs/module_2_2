first = int(input('Ввод числа 1: '))
second = int(input('Ввод числа 2: '))
third = int(input('Ввод числа 3: '))
if first == second == third:
    print(3)
elif first == second != third or first != second == third or first == third != second:
    print(2)
elif first != second != third:
    print(0)
