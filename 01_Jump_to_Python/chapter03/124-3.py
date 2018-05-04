# coding: cp949
prompt="""
1.Add
2.Del
3.List
4.Quit

Enter number:"""
number=0
while True:
    print(prompt,end='')
    number=int(input())

    if number ==4:
        break#while문 종료조건이 2개이상일때

