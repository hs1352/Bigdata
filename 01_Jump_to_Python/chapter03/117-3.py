# coding: cp949


money=int(input("�󸶸��������ս��ϱ�?"))
card = input("ī�带 �����ϰ� �ֽ��ϱ�?(y/n): ")

if card == 'y':     card=True
else:               card=False

#�߸�§���α׷�
if money >= 3000:
    print("�ýø�Ÿ����")
else:
    if card == True:
        #print("�ýø�Ÿ����") ������ �ڵ��ϰ���ߺ�
        print("ī������ �ýø� Ÿ�� ����")
    print("�ɾ��")
