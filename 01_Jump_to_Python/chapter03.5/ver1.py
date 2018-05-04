# coding: cp949
num=1
while num != 0:
    print("마름모 출력 프로그램 ver1.0")
    print("홀수를 입력하세요:(0 <-종료): ",end=" ")
    num=int(input())
   
    if num%2==0:
        print("짝수를 입력하셨습니다.재입력하세요.\n")
        continue

    blank=num//2
    star=1
    while True:
        print(" "* blank,end="")
        
        print("*"* star)
        if star==num:
            break
        star+=2
        blank-=1
        


 

        
    


