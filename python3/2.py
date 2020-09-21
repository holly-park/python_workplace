dataList = []

def append():
    global dataList
    while(True):
        temp = {}
        temp['name']=input("이름: ")
        temp['worktime']=int(input("근무시간: "))
        temp['perpay']=int(input("시간당급여액: "))

        dataList.append(temp)
        again = input("계속? 1.yes 2.no")
        if again != "1":
            break

def output():
    global dataList
    for data in dataList:
        print(data['name'], end='\t')
        print(data['worktime'], end='\t')
        print(data['perpay'])

def start():
    while(True):
        print("1.추가")
        print("2.출력")
        print("0.종료")
        menu=input("선택: ")
        if menu=="1":
            append()
        elif menu=="2":
            output()
        else:
            print("프로그램을 종료합니다")
            return

start()