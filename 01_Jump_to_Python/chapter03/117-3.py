# coding: cp949


money=int(input("얼마를가지고잇습니까?"))
card = input("카드를 소유하고 있습니까?(y/n): ")

if card == 'y':     card=True
else:               card=False

#잘못짠프로그램
if money >= 3000:
    print("택시를타고가라")
else:
    if card == True:
        #print("택시를타고가라") 동일한 코드일경우중복
        print("카드지원 택시를 타고 가라")
    print("걸어가라")
