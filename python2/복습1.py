"""
문제1. 주급계산
이름, 근무시간, 시간당급여액, 주급을 계산하는데 만약 근무시간이 40시간이 넘는다면 초과부분에 대해서는
시간당급여액의 50%를 특별수당으로 계산하라
그리고 총 금액이 20만원 미만이면 3.3%로 세금을 계산하고
20만원 이상 40만원 미만이면 4.4%
40만원 이상이면 5.5%로 계산하라
print("홍길동님이 근무한 시간은 ()시간이고 시급은 ()이고 주수령액은()이고 수당은()이고
세금은()으로 실수령액은 () 입니다")
"""

name=input("이름: ")
worktime=int(input("주당근무시간: "))
workpay=int(input("시간당급여액: "))

weekpay=worktime*workpay
overpay=0
if worktime>40:
    overpay=(worktime-40)*0.5
totalpay=weekpay+overpay

if totalpay>=400000
    tax=totalpay*0.055
elif totalpay>=200000
    tax=totalpay*0.044
else:
    tax=totalpay*0.033


realpay=totalpay-tax
result="{} {} {} {} {} {} {} {}".format(name, worktime, workpay,weekpay,overpat,totalpay,tax,realpay)

print(result)