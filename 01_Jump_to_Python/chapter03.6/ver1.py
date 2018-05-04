# coding: cp949
print("나이를 입력하세요.")
num=int(input())
if num<=3:
    num="무료"
elif num<=13:
    num="2000"
elif num<=18:
    num="3000"
elif num<=65:
    num="5000"
elif num>=66:
    num="무료"
print("요금은 %s입니다." %num)
