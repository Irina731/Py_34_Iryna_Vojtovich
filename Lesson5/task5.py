# Создать функцию, которая будет объединять два словаря в один и возвращать его


slov1 = {"Car":"BMV","Car2": "Audi","Car3": "Volvo"}
slov2 = {"City":"Lida","City2": "Minsk","City": "Grodno"}
merget_slov = {}
def Sumslov(a,b):

    for key,value in slov1.items():
        merget_slov[key] = value
    for key,value in slov2.items():
        merget_slov[key] = value
        return merget_slov

print(Sumslov(slov1,slov2))
