# Создать словарь в качестве ключа которого будет 6-ти значное число(id)
# а в  качестве значений кортеж состоящий из 2х
# элементов - имя(str) возраст(int).
# Сдеать около 5 - 6 элементов словаря , записать данный словарь на диск в json-файл

import json

client_basa = {"123456": ('Irina',35),
               "234567":('Olga',19),
               "345678":('Elena',29),
               "456789":('Natali',55),
               "567890":('Maria',33)}

client_basa_json = json.dumps(client_basa)

with open ('client_basa_json','wt', newline= '\n') as f:
    f.write(client_basa_json)
    print(client_basa_json)
