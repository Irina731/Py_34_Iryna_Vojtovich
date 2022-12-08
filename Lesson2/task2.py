import random
user_= input("введите число от 1 до 20: ")
comp_ = random.randint(1,20)
print(comp_)
attempt = 1


while user_ !=  comp_:
    print("Вы не угадали .Введите число еще раз!")
    user_ = int(input("Выберите число от 1 до 20: "))
    print(comp_)

    if user_ == comp_:
        print("Вы угадали число!")




a = list(input("Введите любые отрицательные и положительные числа: "))
plus = []
minus = []
for i in a:
    if int > 0:
        plus.append(i)
    else:
        minus.append(i)
print(f'положительными числами будут {plus}')

print(f'отрицательными числами будут {minus}')