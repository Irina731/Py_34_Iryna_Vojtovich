# Сделать функцию,к-я будет вызываться из генератора списков и по запросу к ней отдавать текущее время
# с задержкой в 1 сек. кол-во эл-тов нового списка n запрашивать у пользователя

import datetime
import time

def TimeData():
    datatime = []
    n = int(input("Введите кол-во элементов: "))
    for i in range(1,n+1):
        time.sleep(1)
        DateNow = datetime.datetime.now()
        DateNowStr = DateNow.strftime('%Y/%m/%d %H:%M:%S')
        datatime.append(DateNowStr)
    print(datatime)
TimeData()

