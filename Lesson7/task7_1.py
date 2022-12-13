# Прочитать сохраненный json-файл и записать данные на диск в csv-файл ,
# первой строкой которого озаглавив каждый столбец и добавивновый столбец "телефон"

import json
import csv

with open("client_basa_json.json","r") as f:
    data = json.loads(j.read())
    keys = list(data.keys())
    values = list(data.values())
    print(key)
    print(values)

    with open ("data.csv" ,"w") as csvf:
        writer =csv.writer(csvf)
        writer.writerow(keys)
        writer.writerow(value)