# coding: cp949
print("���̸� �Է��ϼ���.")
num=int(input())
if num<=3:
    num="����"
elif num<=13:
    num="2000"
elif num<=18:
    num="3000"
elif num<=65:
    num="5000"
elif num>=66:
    num="����"
print("����� %s�Դϴ�." %num)
