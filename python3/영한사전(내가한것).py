Dictionary = []
word = {}
word['mango']='망고'
word['apple']='사과'
Dictionary.append(word)



#검색
def search(Dictionary):
    vocab = input("영어단어를 입력하세요: ")
    if vocab in word: 
        print(Dictionary.values())
    while vocab in word:
        print(Dictionary.values())
      break

#추가    
def append(Dictionary):
    word[vocab]=input("한국어 의미: ")


#시작
def start(Dictionary):
    while(True):
        print("1.검색")
        print("2.추가")
        print("0.종료")
        menu=input("선택: ")
        if menu=="1":
            search(Dictionary)
        elif menu=="2":
            append(Dictionary)
        else:
            print("프로그램을 종료합니다.")
            return


start(Dictionary)

    


