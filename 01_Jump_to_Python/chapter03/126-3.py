# coding: cp949

prompt = """
<SW 아키텍처 커피자판기 Ver1.0>
1.커피구매
2.커피잔량확인
3.프로그램종료
메뉴를선택하세요"""

coffee =10
number = 0
money = 0
while number != 3:
    print(prompt)
    number = int(input())

    if number ==1:
        money = int(input("금액을 입력하세요: "))
        if money < 300:
            print("금액이 %d모자랍니다." %(300-money))
        elif money == 300:
            print("커피를 줍니다.")
            coffee -= 1
        else:
            print("커피를 줍니다.\n여기 거스릅돈 %d 입니다." %(money-300))
            coffee -= 1
    elif number ==2:
        print("남은 커피의 양은 %d개 입니다." % coffee)

