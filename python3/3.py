dataList = list()

def append(dataList):
    while(True):
        temp = dict()
        temp['name']=input("이름: ")
        temp['worktime']=int(input("근무시간: "))
        temp['perpay']=int(input("시간당급여: "))

        dataList.append(temp)
        again = input("계속?")