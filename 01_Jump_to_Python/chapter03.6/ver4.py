# coding: cp949
"""
0~3��(����):����
4~13��(���): 2000��
14~18��(û�ҳ�): 3000��
19~65��(����): 5000��
66�� �̻�(����): ����

���ѷ��� ��Ʈ��c
"""

while True:
    
    while True:
        print("���̸� �Է��ϼ���.: ",end="")
        age=int(input())
        if age<0:
            print("�ٽ��Է��ϼ���")
            continue
        break
    if age<=3:
        charge="����"
        grade="����"
    elif age<=13:
        charge=2000
        grade="���"
    elif age<=18:
        charge=3000
        grade="û�ҳ�"
    elif age<=65:
        charge=5000
        grade="����"
    elif age>=66:
        charge="����"
        grade="����"
    print("������ %s����̸� ����� %s�Դϴ�." %(grade,charge))
   
    if charge !="����":
        print("��� ������ �����ϼ���.(1:����, 2:���� ����ſ� ī��): ",end="")
        cash=int(input())
    while grade!="����" and grade!="����" and cash==1:
        print("����� �Է��ϼ���: ",end="")
        pay=int(input())

        if pay<charge:
            print("%s�� ���ڶ��ϴ�. �Է��Ͻ� %s�� ��ȯ�մϴ�." %(charge-pay,pay))
            break
        elif pay==charge:
            print("�����մϴ�.Ƽ���� �����մϴ�.")
            break
        else:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s�� ��ȯ �մϴ�." %(pay-charge))
            break

    while grade!="����" and grade!="����" and cash==2:

        """(���� �ݾ��� 10% ����, 60~65�� ����� �߰� 5% ����)"""
        if grade=="���" or "û�ҳ�" or (grade=="����" and age<60):
            print("%0.0f�� ���� �Ǿ����ϴ�." %(float(charge)-(float(charge)*0.1)))
            break
        else:
            print("%0.0f�� ���� �Ǿ����ϴ�." %(float(charge)-(float(charge)*0.1)-(float(charge)*0.05)))
            break
  

    
