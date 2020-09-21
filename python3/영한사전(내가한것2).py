#단어를 모두 저장하기위한 변수 - 사전 객체 저장
mydic = {}
def __init__(mydic):
    mydic['survey']='조사하다'
    mydic['flower']='꽃'
    mydic['cloud']='구름'
    mydic['rain']='비'
    mydic['rainbow']='무지개'
    mydic['wind']='바람'
    mydic['law']='법'
    

def search(mydic):
    key = input("단어: ")
    if key in mydic:
        print(key, "===>", mydic[key])
    else:
        print("해당 단어가 없습니다.")


def append(mydic):
    key = input("영단어:  ")
    value = input("한글:  ")

    mydic[key]=value
    

def output(mydic):
    for key in mydic: #파이썬 키값만 차례로 던져준다
        print(key, "===>", mydic[key])


"""
__init__(mydic)
append(mydic)
output(mydic)
"""



def menuDisplay():
    print("--------")
    print("  선택  ")
    print("--------")
    print("1.검색")
    print("2.추가")
    print("3.수정")
    print("4.삭제")
    print("5.전체보기")
    print("6.종료")

def correct(mydic):
    pass


def  delete(mydic):
    del mydic[]


def start(mydic):
    __init__(mydic)
    while(True):
        menuDisplay()
        sel = input("선택")
        if sel=="1":
            search(mydic)
        elif sel=="2":
            append(mydic)
        elif sel=="3":
            correct(mydic)
        elif sel=="4":
            delete(mydic)
        elif sel=="5":
            output(mydic)
        else:
            break


start(mydic)