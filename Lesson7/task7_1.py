# Прочитать сохраненный json-файл и записать данные на диск в csv-файл ,
# первой строкой которого озаглавив каждый столбец и добавивновый столбец "телефон"

import json
import csv

with open("client_basa_json_1.json","r") as f:
    json_f = f.read()
    print(json_f)


     with open ("data.csv" ,"w") as csvf:
         writer =csv.writer(csvf)