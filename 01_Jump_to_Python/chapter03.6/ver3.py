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
    
    while grade!="����" and grade!="����":
        print("����� �Է��ϼ���: ",end="")
        pay=int(input())

        if grade=="���" and pay<charge:
            print("%s�� ���ڶ��ϴ�. �Է��Ͻ� %s�� ��ȯ�մϴ�." %(charge-pay,pay))
            break
        elif grade=="���" and pay==charge:
            print("�����մϴ�.Ƽ���� �����մϴ�.")
            break
        elif grade=="���":
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s�� ��ȯ �մϴ�." %(pay-charge))
            break



        if grade=="û�ҳ�" and pay<charge:
            print("%s�� ���ڶ��ϴ�. �Է��Ͻ� %s�� ��ȯ�մϴ�." %(charge-pay,pay))
            break
        elif  grade=="û�ҳ�" and pay==charge:
            print("�����մϴ�.Ƽ���� �����մϴ�.")
            break
        elif  grade=="û�ҳ�":
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s�� ��ȯ �մϴ�." %(pay-charge))
            break


        if grade=="����" and pay<charge:
            print("%s�� ���ڶ��ϴ�. �Է��Ͻ� %s�� ��ȯ�մϴ�." %(charge-pay,pay))
            break
        elif  grade=="����" and pay==charge:
            print("�����մϴ�.Ƽ���� �����մϴ�.")
            break
        elif  grade=="����":
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s�� ��ȯ �մϴ�." %(pay-charge))
            break

    