# coding: cp949

prompt = """
<SW ��Ű��ó Ŀ�����Ǳ� Ver1.0>
1.Ŀ�Ǳ���
2.Ŀ���ܷ�Ȯ��
3.���α׷�����
�޴��������ϼ���"""

coffee =10
number = 0
money = 0
while number != 3:
    print(prompt)
    number = int(input())

    if number ==1:
        money = int(input("�ݾ��� �Է��ϼ���: "))
        if money < 300:
            print("�ݾ��� %d���ڶ��ϴ�." %(300-money))
        elif money == 300:
            print("Ŀ�Ǹ� �ݴϴ�.")
            coffee -= 1
        else:
            print("Ŀ�Ǹ� �ݴϴ�.\n���� �Ž����� %d �Դϴ�." %(money-300))
            coffee -= 1
    elif number ==2:
        print("���� Ŀ���� ���� %d�� �Դϴ�." % coffee)

