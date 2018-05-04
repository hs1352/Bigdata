# coding: cp949
"""0~3세(유아):무료
4~13세(어린이): 2000원
14~18세(청소년): 3000원
19~65세(성인): 5000원
66세 이상(노인): 무료
무한루프 컨트롤c"""
count=1
freeticket=3
coupon=5
pay=0
charge=0
cash=0
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

    if grade=="유아" or grade=="노인":
        continue
    if pay>=charge: count+=1
    if cash==2: count+=1
    
    if count%7==0 and freeticket>0:
        freeticket-=1
        print("축하합니다. 1주년 이벤트에당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %s장"%freeticket)
        continue
    if count%4==0 and coupon>0:
        coupon-=1
        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여티켓 %s장"%coupon)
        continue

    if charge !="무료":
        print("요금 유형을 선택하세요.(1:현금, 2:공원 전용신용 카드): ",end="")
        cash=int(input())
    while cash==1:
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

    while cash==2:
        
        """(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)"""
        if age<60:
            print("%0.0f원 결제 되었습니다." %(float(charge)-(float(charge)*0.1)))
            break
        else:
            print("%0.0f원 결제 되었습니다." %(float(charge)-(float(charge)*0.1)-(float(charge)*0.05)))
            break
   
    
    
    

