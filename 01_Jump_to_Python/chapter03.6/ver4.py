# coding: cp949
"""
0~3세(유아):무료
4~13세(어린이): 2000원
14~18세(청소년): 3000원
19~65세(성인): 5000원
66세 이상(노인): 무료

무한루프 컨트롤c
"""

while True:
    
    while True:
        print("나이를 입력하세요.: ",end="")
        age=int(input())
        if age<0:
            print("다시입력하세요")
            continue
        break
    if age<=3:
        charge="무료"
        grade="유아"
    elif age<=13:
        charge=2000
        grade="어린이"
    elif age<=18:
        charge=3000
        grade="청소년"
    elif age<=65:
        charge=5000
        grade="성인"
    elif age>=66:
        charge="무료"
        grade="노인"
    print("귀하의 %s등급이며 요금은 %s입니다." %(grade,charge))
   
    if charge !="무료":
        print("요금 유형을 선택하세요.(1:현금, 2:공원 전용신용 카드): ",end="")
        cash=int(input())
    while grade!="유아" and grade!="노인" and cash==1:
        print("요금을 입력하세요: ",end="")
        pay=int(input())

        if pay<charge:
            print("%s가 모자랍니다. 입력하신 %s를 반환합니다." %(charge-pay,pay))
            break
        elif pay==charge:
            print("감사합니다.티켓을 발행합니다.")
            break
        else:
            print("감사합니다. 티켓을 발행하고 거스름돈 %s를 반환 합니다." %(pay-charge))
            break

    while grade!="유아" and grade!="노인" and cash==2:

        """(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)"""
        if grade=="어린이" or "청소년" or (grade=="성인" and age<60):
            print("%0.0f원 결제 되었습니다." %(float(charge)-(float(charge)*0.1)))
            break
        else:
            print("%0.0f원 결제 되었습니다." %(float(charge)-(float(charge)*0.1)-(float(charge)*0.05)))
            break
  

    
