mylist=[50, -8, 90, 44, 71, 19, 42]
for i in range(len(mylist)):
    for m in range(len(mylist)):
        if mylist[i]<mylist[m]:
            mylist[i], mylist[m] = mylist[m], mylist[i]
print(mylist)




# Дано целое число. Написать программу, которая будет отображать сумму его цифр.

x = input('Введите целое число: ')
Sum = 0
for i in x:
    Sum += int(i)
print(Sum)



# Дано целое число. Написать программу, которая будет отображать произведение его цифр.

x = int(input('Введите целое число: '))
x_ = str(x)
result = 1
for i in x_:
    result *= int(i)
    print(result)



# Создать функцию SumRange(start, end), которая будет суммировать все целые числа от start до end.Дополнительно:
# Обработать следующий случай: Если пользователь задаст значение start больше, чем end,
# то они будут меняться местами.
#
def SumRange(start,end):
    return start + end

total = SumRange(15,9)
print(total)

def sum_range(start, end):
    if start > end:
        start, end = end, start
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum
a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
print(sum_range(a, b))
