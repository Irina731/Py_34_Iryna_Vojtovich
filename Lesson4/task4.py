# Создать функцию для генерации списков.Функция должна возвращать сгенерированный список чисел
# Пример использования функции:
# A = Generator(start = 10, stop = 20, step = 2)
# #### A[10,12,14,16,18]A = Generator(start = 5, stop = 10) #### A[5,6,7,8,9]

def Generator(start: int,stop: int,step: int):
    x = [i for i in range(a,b+1,c)]
    return x

a = int(input("Введите первое число: "))
b = int(input("Введите конечное число: "))
c = int(input("Введите шаг: "))
Generator(a,b,c)
print(f'start = ',a,'stop = ',b,'step = ',c)
print(Generator(a,b,c))



#дан словарь,создать новый словарь,поменяв местами ключ и значение

slov1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(slov1)
print({values:key for key,values in slov1.items()})

