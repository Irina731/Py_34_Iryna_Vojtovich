x = float(2.50)
y = float(3.8)
x_ = abs(x)
y_ = abs(y)
print((x_ - y_)/(1 + x_*y_))



A = 10
B = 10
if A == B:
    print("True")
else:
    print("False")
a_id = id(A)
b_id = id(B)
a_id = str("10")
b_id = str("10")
if a_id == b_id:
    print("True")
else:
    print("False")




x = (input("Сделайте выбор: камень ,ножницы  или бумага: "))

import random
y = random.choice(["камень","ножницы","бумага"])
print(y)
if x == y:
    print("Ничья")

elif x == "камень":
    if y == "ножницы":
        print("Вы победили!")
    else:
        print("Вы проиграли.")

elif x == "бумага":
    if y == "камень":
         print("Вы победили!")
    else:
        print("Вы проиграли.")
elif x == "ножницы":
    if y == "бумага":
        print("Вы победили!")
    else:
        print("Вы проиграли.")