# coding: cp949
num=1
while num !=0:
    print("마름모 출력 프로그램 ver2.0")
    print("홀수를 입력하세요:(0 <- 종료): ", end=" ")
    num=int(input())

    if num%2==0:
        print("짝수를 입력하셨습니다.재입력하세요\n")
        continue


    print("-"*num+"--")

    blank=num//2
    star=1
    while True:
        print("|",end="")
        print(" "* blank,end="")
        print("*"* star,end="")
        print(" "* blank,end="")
        print("|")
        if star==num:
            break
        star+=2
        blank-=1
        
    
    blank=1
    star=num-2
    while True:
        
        if star<0:
            break     
        print("|",end="")
        print(" "* blank,end="")
        print("*"* star,end="")
        print(" "* blank,end="")
        print("|")
        star-=2
        blank+=1
    
    print("-"*num+"--")
