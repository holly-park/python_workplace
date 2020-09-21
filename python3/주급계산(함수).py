"""
이름, 근무시간, 시간당급여액, 총액, 수당, 세금
방법1.전역변수
방법2.매개변수
방법3.객체지향 class
"""


#방법1
dataList = list() #전역변수로 씀

def append():
    global dataList #함수간에 공유 메모리
    while(True):
        temp = dict() #dict타입 객체 만들고
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
        print(data['perpay'], end='\t')

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
            print("프로그램을 종료합니다.")
            return


start()

