# coding: cp949
"""0~3��(����):����
4~13��(���): 2000��
14~18��(û�ҳ�): 3000��
19~65��(����): 5000��
66�� �̻�(����): ����
���ѷ��� ��Ʈ��c"""
count=1
freeticket=3
coupon=5
pay=0
charge=0
cash=0
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

    if grade=="����" or grade=="����":
        continue
    if pay>=charge: count+=1
    if cash==2: count+=1
    
    if count%7==0 and freeticket>0:
        freeticket-=1
        print("�����մϴ�. 1�ֳ� �̺�Ʈ����÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %s��"%freeticket)
        continue
    if count%4==0 and coupon>0:
        coupon-=1
        print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ�Ƽ�� %s��"%coupon)
        continue

    if charge !="����":
        print("��� ������ �����ϼ���.(1:����, 2:���� ����ſ� ī��): ",end="")
        cash=int(input())
    while cash==1:
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

    while cash==2:
        
        """(���� �ݾ��� 10% ����, 60~65�� ����� �߰� 5% ����)"""
        if age<60:
            print("%0.0f�� ���� �Ǿ����ϴ�." %(float(charge)-(float(charge)*0.1)))
            break
        else:
            print("%0.0f�� ���� �Ǿ����ϴ�." %(float(charge)-(float(charge)*0.1)-(float(charge)*0.05)))
            break
   
    
    
    

