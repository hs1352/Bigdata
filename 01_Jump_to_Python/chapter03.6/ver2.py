# coding: cp949
"""
0~3세(유아):무료
4~13세(어린이): 2000원
14~18세(청소년): 3000원
19~65세(성인): 5000원
66세 이상(노인): 무료
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
        charge="2000"
        grade="어린이"
    elif age<=18:
        charge="3000"
        grade="청소년"
    elif age<=65:
        charge="5000"
        grade="성인"
    elif age>=66:
        charge="무료"
        grade="노인"
    print("귀하의 %s등급이며 요금은 %s입니다." %(grade,charge))

