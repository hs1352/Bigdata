# coding: cp949
card = input("카드를 소유하고 있습니까?(y/n): ")
partnership = input("아키첵처 택시 전용입니까? (y/n)")

if card == 'y':     card=True
else:               card=False
if partnership == 'y':      partnership = True
else:                       partnership = False

if card == True:
    if partnership == True:
        print("택시를타고가라")
    else:
        print("멤머쉽 카드가 아니므로 걸어가셔야 합니다.")
else:
    print("걸어가셔야 합니다.")
