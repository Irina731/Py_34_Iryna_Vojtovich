# Прочитать сохраненный json-файл и записать данные на диск в csv-файл ,
# первой строкой которого озаглавив каждый столбец и добавивновый столбец "телефон"

import json
import csv


with open ('client_basa_json_1.json',"r") as f:
    json_f = f.read()
    print(json_f)


with open("data.csv","w") as csvf:
    fieldnames = ["Id","Name","Are","Telefon"]
    writer = csv.DictWriter(csvf,fieldnames= fieldnames)
    writer.writeheader()
    writer.writerows([{"Id":'123456', 'Name':'Irina','Are': '35','Telefon':'None'},
                      {'Id':"234567","Name":" Olga", "Are":"19", "Telefon": "None"},
    {'Id':"345678","Name":" Elena", "Are":"29", "Telefon": "None"},
    {'Id':"456789","Name":" Natali" ,"Are":"55", "Telefon": "None"},
                      {'Id':"567890","Name":" Maria" ,"Are":"33", "Telefon": "None"}])









