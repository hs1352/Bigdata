# coding: cp949


money=int(input("얼마를가지고잇습니까?"))
card = input("카드를 소유하고 있습니까?(y/n): ")

if card == 'y':     card=True
else:               card=False

#잘못짠프로그램
if money >= 3000:
    print("택시를타고가라")
elif card == True:
    print("택시를 타고가라")
else:
    print("걸어가라")
